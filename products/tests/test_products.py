# We want to make sure we only get the products with a price higher than -1.0
# We want to make sure we only get the products with a valid title
# We want to make sure we only get the products with an image
# We want to make sure we only get the products with a proper link (Check if "www.amazon.com" is in the link)
# We want to make sure we only get the products with currency dollars (Check if "$" is in the currency)
# Let's say for some reason we want to get higher price products so that we could get a higher commission from Amazon if someone is buying a product through our link. (Check if the price is not lower than $5)

import unittest
from typing import Dict, List
from unittest.mock import Mock, patch

import requests
from parse import Products
from request import ProductRequest


class MockResponse:
    def __init__(self):
        pass

    def get_product(
        self,
        current_price: float,
        title: str,
        asin: str,
        image: str,
        full_link: str,
        reviews: int,
        prime: bool,
        sponsored: bool
    ) -> Dict:
        return {
            'asin': asin,
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices': {'current_price': current_price,
                       'previous_price': -1.0,
                       'currency': '$'},
            'reviews': reviews,
            'prime': prime,
            'sponsored': sponsored
        }

    def get_product_price_higher_than_minus_one(self, *args, **kwargs) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200
        import product_features_fromamazon as pix

        # title: List = [
        #     pix.pixel_data['results'][enum]['title']
        #     for enum in range(10)
        # ]
        # print(title)

        invalid_price_products: List = [
            self.get_product(
                current_price=-1.0,
                title=pix.pixel_data['results'][enum]['title'],
                asin=pix.pixel_data['results'][enum]['asin'],
                image=pix.pixel_data['results'][enum]['image'],
                full_link=pix.pixel_data['results'][enum]['full_link'],
                reviews=pix.pixel_data['results'][enum]['reviews']['stars'],
                prime=pix.pixel_data['results'][enum]['prime'],
                sponsored=pix.pixel_data['results'][enum]['sponsored']
            ) for enum in range(10)
            # for _ in range(10)
        ]

        valid_price_products: List = [
            self.get_product(
                current_price=435.45,
                title=pix.pixel_data['results'][enum]['title'],
                asin=pix.pixel_data['results'][enum]['asin'],
                image=pix.pixel_data['results'][enum]['image'],
                full_link=pix.pixel_data['results'][enum][
                    'full_link'],
                reviews=
                pix.pixel_data['results'][enum]['reviews']['stars'],
                prime=pix.pixel_data['results'][enum]['prime'],
                sponsored=pix.pixel_data['results'][enum]['sponsored']
            ) for enum in range(10)
        ]
        products = invalid_price_products + valid_price_products

        mock_response.json.return_value = {
            'results': products
        }
        return mock_response

    def get_mock_response() -> Dict:
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

    @patch.object(
        target=requests,
        attribute='get',
        # side_effect=[Mock(**get_mock_response())]
        side_effect=MockResponse().get_product_price_higher_than_minus_one
    )
    def test_price_greater_than_minus_one(self, *args, **kwargs):
        request = ProductRequest()
        res: requests.Response = request.get(params={
            'country': 'US',
            'query': 'Pixel',
            'page': 1
        }
        )
        res_data: Dict = res.json()
        print(res_data)

        products = Products(data=res_data, amount=5).get()
        for product in products:
            self.assertNotEqual(product['price'], -1.0)
            print(product)

        # print(products)

    def test_valid_title(self):
        pass
