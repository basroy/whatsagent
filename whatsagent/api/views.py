import typing
import json
from django.http.request import HttpRequest
from django.http.response import JsonResponse


from whatsagent.api.serializers.serializers import SignupSerializer
from whatsagent.api.enums import common as enums
from whatsagent.api.exceptions import common as exceptions

from rest_framework import serializers
from whatsagent.api.models import User

# Utility to use gmail api
import googleapiclient.errors
from django.conf import settings
import ssl
import smtplib
from email.message import EmailMessage as pymail

from rest_framework.decorators import api_view

from django.db.transaction import atomic


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

        smtp.login(
            user=email_sender,
            password=settings.GMAIL_SENDER_APP_KEY
        )

        return_sendmail = smtp.sendmail(
            from_addr='bashobi@gmail.com',
            to_addrs=email_receiver,
            msg=gm.as_string()
        )
        if len(return_sendmail) == 0:
            return enums.EmailStatus.SUCCESS.value
        else:
            return enums.EmailStatus.FAILURE.value
    except (
            ValueError,
            googleapiclient.errors.HttpError,
            smtplib.SMTPRecipientsRefused
    ) as e:

        return enums.EmailStatus.FAILURE.value


@api_view(['POST'])
@atomic
def user_signup(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)
    serializer = SignupSerializer(data=signup_data)
    serializer.is_valid(raise_exception=True)
    signup_fields: typing.Dict = serializer.data

    user_exists: bool = (
        User
            .objects
            .filter(email=signup_fields['email'].lower())
            .exists()
    )

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

    user: User = User.objects.create_user(
        signup_fields['name'],
        signup_fields['terms'],
        signup_fields['email'].lower(),
        signup_fields['password']
    )
    email_status = send_message(
        email_sender='Bashobi',
        email_receiver=user.email,
        email_subject='User signup notification',
        email_body=(
            'You have successfully signed up'
        )
    )
    if email_status == enums.EmailStatus.SUCCESS.value:
        return JsonResponse(
            status=201,
            data={
                'detail':
                    f'Signup was successful, registration email was sent to '
                    f'{user.email}'
            }
        )
    else:
        raise exceptions.ServiceUnavailable()


