# We want to make sure we only get the products with a price higher than -1.0
# We want to make sure we only get the products with a valid title
# We want to make sure we only get the products with an image
# We want to make sure we only get the products with a proper link (Check if "www.amazon.com" is in the link)
# We want to make sure we only get the products with currency dollars (Check if "$" is in the currency)
# Let's say for some reason we want to get higher price products so that we could get a higher commission from Amazon if someone is buying a product through our link. (Check if the price is not lower than $5)

import unittest
from typing import Dict
from unittest.mock import Mock, patch

import requests

from products.parse import Product
from products.request import ProductRequest


def get_mock_response() -> Dict:
    return {
        'status_code': 200,
        'json.return_value': {'results': [
            {'asin': 'FAKE_B09JJ1NKDK',
             'title': f'Google Pixel 4 (128GB, 6GB) 5.7", IP68 Water '
                      f'Resistant, Snapdragon 855, GSM/CDMA Factory Unlocked '
                      f'(AT&T/T-Mobile/Verizon/Fi) w/Fast Qi Wireless Pad '
                      f'(Clearly White)',
             'image': (
                 f'https://m.media-amazon.com/images/I/517rGuQMegL'
                 f'._AC_UY218_.jpg'
             ),
             'full_link': 'https://www.amazon.com/dp/B09JJ1NKDK/?psc=1',
             'prices': {'current_price': 459.99, 'previous_price': -1.0,
                        'currency': '$'},
             'reviews': {'total_reviews': 34, 'stars': 3.8},
             'prime': False,
             'sponsored': True}
        ]}
    }


class TestProductFeature(unittest.TestCase):
    test_data: Mock = Mock()

    @patch.object(
        target=requests,
        attribute='get',
        side_effect=[
            Mock(**get_mock_response())
        ]
    )
    #                                                                   {
    #     'status_code': 200,
    #     'json.return_value': {'results': [
    #         {'asin': 'FAKE_B09JJ1NKDK',
    #          'title': 'Google Pixel 4 (128GB, 6GB) 5.7", IP68 Water Resistant, Snapdragon 855, GSM/CDMA Factory Unlocked (AT&T/T-Mobile/Verizon/Fi) w/Fast Qi Wireless Pad (Clearly White)',
    #          'image': 'https://m.media-amazon.com/images/I/517rGuQMegL._AC_UY218_.jpg',
    #          'full_link': 'https://www.amazon.com/dp/B09JJ1NKDK/?psc=1',
    #          'prices': {'current_price': 459.99, 'previous_price': -1.0,
    #                     'currency': '$'},
    #          'reviews': {'total_reviews': 34, 'stars': 3.8}, 'prime': False,
    #          'sponsored': True}, {'asin': 'B08C4BXY41',
    #                               'title': "Mobile Pixels Trio Max Portable Monitor, 14'' Full HD IPS Dual Triple Monitor for laptops, USB C/USB A Portable Screen,Windows/Mac/OS/Android/Switch Compatible (1x Monitor Only)",
    #                               'image': 'https://m.media-amazon.com/images/I/81uySvxGB4L._AC_UY218_.jpg',
    #                               'full_link': 'https://www.amazon.com/dp/B08C4BXY41/?psc=1',
    #                               'prices': {'current_price': 309.0,
    #                                          'previous_price': 329.0,
    #                                          'currency': '$'},
    #                               'reviews': {'total_reviews': 997,
    #                                           'stars': 4.1},
    #                               'prime': False, 'sponsored': True}]}
    # })])
    #

    def test_price_greater_than_minus_one(
        self,
        *args,
        **kwargs) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        request = ProductRequest()
        res_from_api: requests.Response = request.get(params={
            'country': 'US',
            'query': 'Pixel',
            'page': '1'})
        print(res_from_api.json())

        res_data = res_from_api.json()
        get_product = Product(data=res_data, amount=-1.0, validity=True)
        valid_products: List = get_product.get_product_detail()

        get_product = Product(data=res_data, amount=-1.0, validity=False)
        invalid_products: List = get_product.get_product_detail()

        print(valid_products)
        print(invalid_products)
        return mock_response

    # def test_price_greater_than_minus_one(self, mock_requests):
    #     request = ProductRequest()
    #     res_from_api: requests.Response = request.get(params={
    #         'country': 'US',
    #         'query': 'Pixel',
    #         'page': '1'})
    #     print(res_from_api.json())
    #
    #     res_data = res_from_api.json()
    #     get_product = Product(data=res_data, amount=-1.0)
    #     products = get_product.get_product()
    #     print(products)

    def test_valid_title(self):
        pass
