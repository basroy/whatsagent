

import unittest
from typing import Dict, List
from unittest.mock import Mock, patch

import products.product_features_fromamazon as pix
import requests
import random
from products.parse import Products
from products.request import ProductRequest


class MockResponse:

    def __init__(self):
        pass

    def get_product(
            self,
            current_price: float,

            title: str = 'Google Pixel 4a with 5G - Android Phone',
            image: str = 'https://m.media-amazon.com/images/I/'
                         '71C0OH4WfpL._AC_UY218_.jpg',
            full_link: str = 'https://www.amazon.com/dp/B08H8VZ6PV/?psc=1',
            currency: str = '$'

    ) -> Dict:

        return {
            'asin': 'B09JJ1NKDK',
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices': {'current_price': current_price,
                       'previous_price': -1.0,
                       'currency': currency},
            'reviews': 3.8,
            'prime': False,
            'sponsored': True
        }

    def get_products(self, invalid_products: List) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        invalid_price_products: List = invalid_products

        valid_price_products: List = [
            self.get_product(current_price=435.04) for _ in range(10)
        ]
        products = invalid_price_products + valid_price_products
        random.shuffle(products)

        mock_response.json.return_value = {
            'results': products
        }
        return mock_response


    def get_product_price_higher_than_minus_one(self, *args, **kwargs) -> Mock:

        invalid_price_products: List = [
            self.get_product( current_price=-1.0) for _ in range(10)
        ]

        return  self.get_products(invalid_products=invalid_price_products)

    def get_product_valid_and_invalid_title(self, *args, **kwargs) -> Mock:

        invalid_title_products: List = [
            self.get_product( current_price=435.0, title='') for _ in range(10)
        ]
        # print(invalid_title_products)
        return self.get_products(invalid_products=invalid_title_products)

    def get_product_valid_and_invalid_image(self, *args, **kwargs) -> Mock:

        invalid_image_products_null: List = [
            self.get_product( current_price=435.0, image='') for _ in range(5)
        ]

        invalid_image_products_incorrect: List = [
            self.get_product(
                current_price=435.0,
                image='amazonjjjji.peg'
            ) for _ in range(5)
        ]
        invalid_image_products = (
                invalid_image_products_null + invalid_image_products_incorrect
        )
        return self.get_products(invalid_products=invalid_image_products)

    def get_product_valid_and_invalid_url(self, *args, **kwargs) -> Mock:

        invalid_url_products: List = [
            self.get_product(
                current_price=435.6,
                full_link='www.amazon-direct.com'
            ) for _ in range(10)
        ]
        return self.get_products(invalid_products=invalid_url_products)

    def get_product_valid_and_invalid_currency(self, *args, **kwargs) -> Mock:

        invalid_currency_products: List = [
            self.get_product(
                current_price=435.0,
                currency='EUR'
            ) for _ in range(10)
        ]
        return self.get_products(invalid_products=invalid_currency_products)

    def get_product_high_valued(self, *args, **kwargs) -> Mock:

        high_valued_products: List = [
            self.get_product(current_price=400.01) for _ in range(10)
        ]
        return self.get_products(invalid_products=high_valued_products)


    def get_mock_response(self) -> Dict:
        return {
            'status_code': 200,
            'json.return_value': {
                'results': [
                    {
                        'asin': 'FAKE_B09JJ1NKDK',
                        'title': f'Google Pixel 4 (128GB, 6GB) 5.7", IP68 Water '
                                 f'Resistant, Snapdragon 855, GSM/CDMA Factory Unlocked '
                                 f'(AT&T/T-Mobile/Verizon/Fi) w/Fast Qi Wireless Pad '
                                 f'(Clearly White)',
                        'image': (
                            f'https://m.media-amazon.com/images/I/517rGuQMegL'
                            f'._AC_UY218_.jpg'
                        ),
                        'full_link': 'https://www.amazon.com/dp/B09JJ1NKDK/?psc=1',
                        'prices': {'current_price': 459.99,
                                   'previous_price': -1.0,
                                   'currency': '$'},
                        'reviews': {
                            'total_reviews': 34,
                            'stars': 3.8
                        },
                        'prime': False,
                        'sponsored': True
                    }
                ]
            }
        }


class TestProduct(unittest.TestCase):


    def execute_request_and_get_product(self) -> List:

        request = ProductRequest()
        res: requests.Response = request.get(
            params={
            'country': 'US',
            'query': 'Pixel',
            'page': 1
        }
        )
        res_data: Dict = res.json()
        return Products(data=res_data, amount=5).get()


    def test_price_greater_than_minus_one(self):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_price_higher_than_minus_one
        )
        with mocked_product_request:
            products: List = self.execute_request_and_get_product()

        for product in products:
            self.assertNotEqual(product['price'], -1.0)


    def test_valid_title(self):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_valid_and_invalid_title
        )
        with mocked_product_request:
            products = self.execute_request_and_get_product()
        for product in products:
            self.assertNotEqual(len(product['title']),0)
            print(f'Title related --> {product}')

    def test_valid_image(self):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_valid_and_invalid_image
        )
        with mocked_product_request:
            products = self.execute_request_and_get_product()
        for product in products:
            self.assertNotEqual(len(product['image']),0)


    def test_valid_url(self):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_valid_and_invalid_url
        )
        with mocked_product_request:
            products = self.execute_request_and_get_product()
        for product in products:
            self.assertNotEqual(len(product['url']),0)


    def test_valid_currency(self):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_valid_and_invalid_currency
        )
        with mocked_product_request:
            products = self.execute_request_and_get_product()
        for product in products:
            self.assertNotEqual(len(product['currency']),'EUR')


    def test_price_higher_than_minimum(self, *args, **kwargs):
        mocked_product_request = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_product_high_valued
        )
        with mocked_product_request:
            products =  self.execute_request_and_get_product()
        for product in products:
            self.assertLessEqual(product['price'],450.19)
