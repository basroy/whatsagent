from typing import Dict, List

import requests


# Macbook-Pro = 21
# Pixel = 22

#
# data: Dict = response.json()
# print(len(response.json()['results']))
# print(response.json()['results'][0].get('title'))
# print(response.json()['results'][0].get('image'))
# print(response.json()['results'][0].get('full_link'))
# print(response.json()['results'][0].get('prices'))


class ProductRequest:

    def __init__(self):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '0865b69e3cmsh8811b8ee5d1546ap1b1727jsne2723b46edf4'
        }
        self.timeout = 20

    def _request(self, method: str, **kwargs) -> requests.Response:
        kwargs.update({
            'timeout': self.timeout
        })
        return getattr(requests, method)(**kwargs)
        # return requests.get(
        #     url=self.url,
        #     headers=self.headers,
        #     params={
        #         'country': 'US',
        #         'query': 'Pixel',
        #         'page': '1'}
        # )

    def get(self, params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params
        )

    def get_product(self):
        pass


data: Dict = {
    'country': 'US',
    'query': 'Pixel',
    'page': '1'
}
request = ProductRequest()
res: requests.Response = request.get(params=data)

res_data: Dict = res.json()
product_names: List = ['AlphaGo', 'Zlatan', 'Pixel']
# print(res_data['results'][0].get('title'))

product_features: Dict = {
    'title': res_data['results'][0].get('title'),
    'url': res_data['results'][0].get('full_link'),
    'price': res_data['results'][0].get('prices'),
    'image': res_data['results'][0].get('image')
}
product: List = [
    product_features
]
