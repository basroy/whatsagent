from typing import Dict

import requests


class ProductRequest:

    def __init__(self, ):
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

    def get(self, params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params
        )
