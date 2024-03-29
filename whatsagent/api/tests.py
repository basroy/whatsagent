import json
import smtplib
from typing import Dict, List
from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from rest_framework.response import Response
from rest_framework.test import APIClient

from .models import User


class MockResponse:

    def __init__(self):
        pass

    def get_invoice_email(self, email: List) -> Dict:
        import whatsagent.settings as sett

        return {
            "from": "bashobiroy",
            "to": email,
            "subject": "Hello Customer",
            'contact_id': sett.GMAIL_SENDER_APP_KEY
        }

    def get_email_mock_success(self) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200
        email: List = ['bashobiroy@yahoo.com']
        mock_response.json.return_value = {
            'details': self.get_invoice_email(email=email),
            'status_desc': 'Email has been successfully sent'
        }

        return mock_response


class TestSignup(TestCase):
    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobiexample.com',
            'password': 'adsfghlColo!',
            'terms': False
        }
        res: Response = client.post(
            path=f'/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'email': [
                    'Enter a valid email address.'
                ]
            }
        )

    def test_password_less_than_min_length(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobi@example.com',
            'password': 'citzq',
            'terms': False
        }
        res: Response = client.post(
            path=f'/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has at least 8 characters.'
                ]
            }
        )

    def test_password_more_than_max_length(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobi@example.com',
            'password': 'citzq,12passwrcitzq',
            'terms': False
        }
        res: Response = client.post(
            path=f'/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has no more than 16 '
                    'characters.'
                ]
            }
        )

    def test_email_already_exists(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobi@example.com',
            'password': 'randopassword1',
            'terms': False
        }

        User.objects.create_user(
            payload['name'],
            payload['terms'],
            payload['email'].lower(),
            payload['password']
        )

        res: Response = client.post(
            path=f'/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.json(),
            {
                'email': [
                    'This email address is already being used.'
                ]
            }
        )

    def test_unaccepted_terms_checkbox(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobi@example.com',
            'password': 'adsfghlColo!',
            'terms': False
        }

        res: Response = client.post(
            path=f'/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'terms': [
                    'You must accept terms and conditions'
                ]
            }
        )

    def test_failed_to_send_email(self):
        client: APIClient = APIClient()
        payload = {
            'name': 'bashobi',
            'email': 'bashobi@gmai.com',
            'password': 'adsfghlColo!',
            'terms': True
        }
        side_effect = {}
        mocked_email = patch.object(
            target=smtplib.SMTP_SSL,
            attribute='login',
            side_effect=smtplib.SMTPRecipientsRefused(side_effect),
        )
        with mocked_email:
            res: Response = client.post(
                path=f'/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )

        self.assertEqual(res.status_code, 503)
        self.assertEqual(res.json(),
                         {
                             'detail': 'Service Unavailable'
                         }
                         )

    def test_successful_signup(self):
        client: APIClient = APIClient()

        payload = {
            'name': 'bashobi',
            'email': 'bashobi@gmail.com',
            'password': 'adsfghlColo!',
            'terms': True
        }

        mocked_email = patch.object(
            target=requests,
            attribute='post',
            side_effect=[MockResponse().get_email_mock_success()]
        )
        with mocked_email:
            res: Response = client.post(
                path=f'/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )

        self.assertEqual(res.status_code, 201)
        user = payload.get('email')
        self.assertEqual(
            res.json(),
            {
                'detail':
                    (
                        f'Signup was successful, '
                        f'registration email was sent to {user}'
                    )
            }
        )
