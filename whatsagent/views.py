import typing
import json

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from whatsagent.serializers import SignupSerializer

from rest_framework import serializers
from whatsagent.api.models import User

# Utility to use gmail api
import googleapiclient.errors
from django.conf import settings
import ssl
import smtplib
from email.message import EmailMessage as pymail
from enum import Enum
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from django.db.transaction import atomic


class EmailStatus(Enum):
    SUCCESS = 'email_sending_success'
    FAILURE = 'email_sending_failure'
    PROGRESS = 'email_sending_in_progress'


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service Unavailable'
    default_code = 'service_unavailable'


@require_http_methods('GET')
def get_sample(r: HttpRequest) -> HttpResponse:
    return HttpResponse(status=200, content=b'sample content')


def send_message(
        email_sender: str,
        email_receiver: str,
        email_subject: str,
        email_body: str
) -> bool:
    gm = pymail()
    gm['From'] = 'Bashobi Roy'
    gm['To'] = email_receiver
    gm['Subject'] = email_subject
    gm.set_content(email_body)
    context = ssl.create_default_context()

    try:
        smtp = smtplib.SMTP_SSL(
            host='smtp.gmail.com',
            port=465,
            context=context
        )
        print(f'SETTINGS --> {settings.GMAIL_SENDER_APP_KEY}')
        smtp.login(
            user=email_sender,
            password=settings.GMAIL_SENDER_APP_KEY
        )
        return_sendmail = smtp.sendmail(
            from_addr='bashobi@gmail.com',
            to_addrs=email_receiver,
            msg=gm.as_string()
        )
        print(f'Standard sendmail status {return_sendmail}')
        if len(return_sendmail) == 0:
            return EmailStatus.SUCCESS.value
        else:
            return EmailStatus.FAILURE.value
    except (
            ValueError,
            googleapiclient.errors.HttpError,
            smtplib.SMTPRecipientsRefused
    ) as e:
        print(f'An error occurred:{e}')
        return EmailStatus.FAILURE.value


# @require_http_methods('POST')
@api_view(['POST'])
@atomic()
def user_signup(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)
    serializer = SignupSerializer(data=signup_data)
    serializer.is_valid(raise_exception=True)
    signup_fields: typing.Dict = serializer.data
    print(signup_fields)
    # User.objects.filter(email=signup_fields['email'].lower()).delete()
    # return JsonResponse(
    #     status=201,
    #     data={
    #         'detail':
    #             f'Signup was successful, registration email was sent to '
    #     }
    # )
    user_exists: bool = (
        User
            .objects
            .filter(email=signup_fields['email'].lower())
            .exists()
    )
    email = (User
        .objects
        .filter(email=signup_fields['email'].lower() )
    )
    # print(f'Does user email exist {user_exists} for {User.objects}')
    if user_exists:
        raise serializers.ValidationError({
            'email':
                [
                    'This email address is already being used.'
                ],
        })
    if not signup_fields['terms']:
        raise serializers.ValidationError({
            'terms':
                [
                    'You must accept terms and conditions'
                ]
        })

    print('Here we are to pass usermodel')
    user: User = User.objects.create_user(
        signup_fields['name'],
        signup_fields['terms'],
        signup_fields['email'],
        signup_fields['password']
    )
    print(user)
    email_status = send_message(
        email_sender='bashobi',
        email_receiver=user.email,
        email_subject='User signup notification',
        email_body=(
            'You have successfully signed up'
        )
    )
    print(f' Email Sent from UI {email_status}')
    if email_status == EmailStatus.SUCCESS.value:
        # print(f'In views {user.email}')
        return JsonResponse(
            status=201,
            data={
                'detail':
                    f'Signup was successful, registration email was sent to '
                    f'{user.email}'
            }
        )
    else:
        raise ServiceUnavailable()

