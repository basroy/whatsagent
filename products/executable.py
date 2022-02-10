from typing import Dict

import requests

import product_features_fromamazon
from products.request import ProductRequest

res_data: Dict = product_features_fromamazon.pixel_data
# request = ProductRequest(data=res_data, amount=-1.0)
request = ProductRequest()
res: requests.Response = request.get(params={
            'country': 'US',
            'query': 'Pixel',
            'page': 1
        })
# print(len(res))
# breakpoint()

with open('products.txt', 'w') as f:
    # f.write(products[i]['current_price'])

    for index, product_detail_from_mockfile in enumerate(products):
        product: str = product_detail_from_mockfile['title']
        cur_price: str = (
            product_detail_from_mockfile['price']['current_price']
        )
        product_url = product_detail_from_mockfile['url']
        product_image = product_detail_from_mockfile['image']

        products_to_file: str = f'Products#{index}' \
                                f'\n\t{product}' \
                                f'\n\t{cur_price}' \
                                f'\n\t{product_url}' \
                                f'\n\t{product_image}\n'

        f.write(products_to_file)
        print(products_to_file)

f.close()
