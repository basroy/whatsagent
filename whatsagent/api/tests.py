
import json

from django.test import TestCase
from rest_framework.response import Response

from unittest.mock import Mock, patch

from rest_framework.test import APIClient
import requests
from typing import Dict, List


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

        mocked_email = patch.object(
            target=requests,
            attribute='post',
            side_effect=requests.HTTPError
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
        print([MockResponse().get_email_mock_success()])
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
