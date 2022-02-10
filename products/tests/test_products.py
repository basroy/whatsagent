# We want to make sure we only get the products with a price higher than -1.0
# We want to make sure we only get the products with a valid title We want to
# make sure we only get the products with an image We want to make sure we
# only get the products with a proper link (Check if "www.amazon.com" is in
# the link) We want to make sure we only get the products with currency
# dollars (Check if "$" is in the currency) Let's say for some reason we want
# to get higher price products so that we could get a higher commission from
# Amazon if someone is buying a product through our link. (Check if the price
# is not lower than $5)

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
            image: str = 'https://m.media-amazon.com/images/I/71C0OH4WfpL._AC_UY218_.jpg',
            full_link: str = 'https://www.amazon.com/dp/B08H8VZ6PV/?psc=1',
            currency: str = '$'

    ) -> Dict:
        enum: int = 3
        return {
            'asin': pix.pixel_data['results'][enum]['asin'],
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices': {'current_price': current_price,
                       'previous_price': -1.0,
                       'currency': currency},
            'reviews': pix.pixel_data['results'][enum]['reviews']['stars'],
            'prime': pix.pixel_data['results'][enum]['asin'],
            'sponsored': pix.pixel_data['results'][enum]['sponsored']
        }

    def get_products(self, invalid_products: List) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        invalid_price_products: List = invalid_products

        #current_price=pix.pixel_data['results'][enum]['prices']['current_price']
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


class TestProductFeature(unittest.TestCase):
    test_data: Mock = Mock()

    def execute_request_and_get_product(self, test_name) -> List:
        # res_data: Dict = pix.pixel_data['results']
        request = ProductRequest()
        res: requests.Response = request.get(
            params={
            'country': 'US',
            'query': 'Pixel',
            'page': 1
        }
        )
        res_data: Dict = res.json()
        # print(res_data)
        # return Products(data=res_data, amount=5).get()
        return Products(data=res_data, amount=5, test_name=test_name).get()

    @patch.object(
        target=requests,
        attribute='get',
        side_effect=MockResponse().get_product_price_higher_than_minus_one
    )
    def test_price_greater_than_minus_one(self, *args, **kwargs):

        products = self.execute_request_and_get_product(test_name='price')
        print(products)
        for product in products:
            print(f'Pricing related --> {product}')
            self.assertNotEqual(product['price'], -1.0)


    @patch.object(
        target=requests,
        attribute='get',
        side_effect=MockResponse().get_product_valid_and_invalid_title
    )
    def test_valid_title(self, *args, **kwargs):
        products = self.execute_request_and_get_product(test_name='title')
        for product in products:
            print(f'Title related --> {product}')
            self.assertNotEqual(len(product['title']),0)

    @patch.object(
                target=requests,
                attribute='get',
                side_effect=MockResponse().
                    get_product_valid_and_invalid_image
    )
    def test_valid_image(self, *args, **kwargs):
        products = self.execute_request_and_get_product(test_name='image')
        for product in products:
            self.assertNotEqual(len(product['image']),0)
            print(f'Image related --> {product}' )

    @patch.object(
                target=requests,
                attribute='get',
                side_effect=MockResponse().
                    get_product_valid_and_invalid_url
    )
    def test_valid_url(self, *args, **kwargs):
        products = self.execute_request_and_get_product(test_name='url')
        for product in products:
            self.assertNotEqual(len(product['url']),0)
            print(f'URL related --> {product}' )

    @patch.object(
                target=requests,
                attribute='get',
                side_effect=MockResponse().
                    get_product_valid_and_invalid_currency
    )
    def test_valid_currency(self, *args, **kwargs):
        products = self.execute_request_and_get_product(test_name='currency')
        for product in products:
            self.assertNotEqual(len(product['currency']),'EUR')


    @patch.object(
                target=requests,
                attribute='get',
                side_effect=MockResponse().
                    get_product_high_valued
    )
    def test_price_higher_than_minimum(self, *args, **kwargs):
        products = self.execute_request_and_get_product(test_name='minimum')
        for product in products:
            self.assertLessEqual(product['price'],450.19)
            print(f'High Value related --> {product}' )