from typing import Dict, List

import requests

import product_features_fromamazon


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

    def __init__(self, data: Dict, amount: float):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '0865b69e3cmsh8811b8ee5d1546ap1b1727jsne2723b46edf4'
        }
        self.timeout = 20
        self.collection = 1
        self.data = data
        self.amount = amount

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

    def get_generic(self, params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params
        )

    # def get_products(self, amazon_res: Dict) -> List:
    # def get(self, amazon_res: Dict, amount: float) -> List:

    def get(self) -> List:
        self.data: Dict = res_data
        # self.amount = amount
        five_of_each: List = []

        # for i in len(res_data):
        for i in range(15):
            product_feature: Dict = {
                'title': res_data['results'][i]['title'],
                'url': res_data['results'][i]['full_link'],
                'price': res_data['results'][i]['prices'],
                'image': res_data['results'][i]['image']
            }

            if product_feature['price']['previous_price'] != self.amount:
                self.collection += 1

                five_of_each.append(product_feature)

            if self.collection > 5:
                break

        return five_of_each


res_data: Dict = product_features_fromamazon.pixel_data
request = ProductRequest(data=res_data, amount=-1.0)
products = request.get()
print(len(products))
with open('products.txt', 'w') as f:
    # f.write(products[i]['current_price'])

    for i in range(len(products)):
        product: str = products[i]['title']
        cur_price: float = products[i]['price']['current_price']
        product_url: str = products[i]['url']
        write_to_file: str = 'Products#' + str(i) + '\n    ' + product + \
                             '\n' + '    Price:' + str(cur_price) + \
                             '\n' + '    Url:' + product_url
        f.write(write_to_file)
        print(write_to_file)

f.close()

# product_feature: Dict = {
#     'title': res_data['results'][i].get('title'),
#     'url': res_data['results'][i].get('full_link'),
#     'price': res_data['results'][i].get('prices'),
#     'image': res_data['results'][i].get('image')
# # }
# res: requests.Response = request.get(params=data)
# res_data: Dict = res.json()
# print(res_data)
