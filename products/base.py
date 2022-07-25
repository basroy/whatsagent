from typing import Dict, List

import requests
import product_features_fromamazon

class ProductRequest:

    def __init__(self, data: Dict, amount: float):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '0865b69e3cmsh8811b8ee5d1546ap1b1727jsne2723b46edf4'
        }
        self.timeout = 20
        self.data = data
        self.amount = amount

    def _request(self, method: str, **kwargs) -> requests.Response:
        kwargs.update({
            'timeout': self.timeout
        })
        return getattr(requests, method)(**kwargs)

    def get(self, params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params
        )

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

    for index, product in enumerate(products):
        title: str = product['title']
        cur_price: str = product['prices']['current_price']

        product_url = product['full_link']
        product_image = product['image']

        products_to_file: str = f'Products#{index}' \
                                f'\n\t{product}' \
                                f'\n\t{cur_price}' \
                                f'\n\t{product_url}' \
                                f'\n\t{product_image}\n'
        f.write(products_to_file)


f.close()


