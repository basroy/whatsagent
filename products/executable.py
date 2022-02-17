from typing import Dict, List

import requests

import product_features_fromamazon
from products.request import ProductRequest


data: Dict = {
        'country': 'US',
        'query': 'Pixel',
        'page': 1
    }

DEBUG = True

if not DEBUG:

    request = ProductRequest()
    res: requests.Response = request.get(params=data)
    res_data: Dict = res.json()
else:
    res_data: Dict = product_features_fromamazon.pixel_data

products: List = res_data['results']

with open('products.txt', 'w') as f:

    for index, product_detail_from_mockfile in enumerate(products):
        product: str = product_detail_from_mockfile['title']
        cur_price: str = (
            product_detail_from_mockfile['prices']['current_price']
        )
        product_url = product_detail_from_mockfile['full_link']
        product_image = product_detail_from_mockfile['image']

        products_to_file: str = f'Products#{index}' \
                                f'\n\t{product}' \
                                f'\n\t{cur_price}' \
                                f'\n\t{product_url}' \
                                f'\n\t{product_image}\n'

        f.write(products_to_file)
        print(products_to_file)

f.close()
