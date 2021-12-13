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

# res_data: Dict = res.json()
# print(res_data)
# All information for Pixel
res_data: Dict = {'error': False,
                  'current_page': 1, 'next_page': 2, 'results': [
        {'asin': 'B09JJ1NKDK',
         'title': 'Google Pixel 4 (128GB, 6GB) 5.7", IP68 Water Resistant, Snapdragon 855, GSM/CDMA Factory Unlocked (AT&T/T-Mobile/Verizon/Fi) w/Fast Qi Wireless Pad (Clearly White)',
         'image': 'https://m.media-amazon.com/images/I/517rGuQMegL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B09JJ1NKDK/?psc=1',
         'prices': {'current_price': 459.99, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 34, 'stars': 3.8}, 'prime': False,
         'sponsored': True}, {'asin': 'B08C4BXY41',
                              'title': "Mobile Pixels Trio Max Portable Monitor, 14'' Full HD IPS Dual Triple Monitor for laptops, USB C/USB A Portable Screen,Windows/Mac/OS/Android/Switch Compatible (1x Monitor Only)",
                              'image': 'https://m.media-amazon.com/images/I/81uySvxGB4L._AC_UY218_.jpg',
                              'full_link': 'https://www.amazon.com/dp/B08C4BXY41/?psc=1',
                              'prices': {'current_price': 309.0,
                                         'previous_price': 329.0,
                                         'currency': '$'},
                              'reviews': {'total_reviews': 997, 'stars': 4.1},
                              'prime': False, 'sponsored': True},
        {'asin': 'B095PY85HG',
         'title': 'Google Pixel 4a - Unlocked Android Smartphone - 128 GB of Storage - Up to 24 Hour Battery - Barely Blue',
         'image': 'https://m.media-amazon.com/images/I/61NrGFKn2LS._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B095PY85HG/?psc=1',
         'prices': {'current_price': 349.0, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 9221, 'stars': 4.6}, 'prime': False,
         'sponsored': False}, {'asin': 'B08H8VZ6PV',
                               'title': 'Google Pixel 4a with 5G - Android Phone - New Unlocked Smartphone with Night Sight and Ultrawide Lens - Just Black',
                               'image': 'https://m.media-amazon.com/images/I/71C0OH4WfpL._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B08H8VZ6PV/?psc=1',
                               'prices': {'current_price': 474.89,
                                          'previous_price': 499.0,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 2288,
                                           'stars': 4.6}, 'prime': False,
                               'sponsored': False}, {'asin': 'B07YMNLXL3',
                                                     'title': 'Google Pixel 4 - Just Black - 64GB - Unlocked',
                                                     'image': 'https://m.media-amazon.com/images/I/713N4SwTtKL._AC_UY218_.jpg',
                                                     'full_link': 'https://www.amazon.com/dp/B07YMNLXL3/?psc=1',
                                                     'prices': {
                                                         'current_price': 377.58,
                                                         'previous_price': -1.0,
                                                         'currency': '$'},
                                                     'reviews': {
                                                         'total_reviews': 877,
                                                         'stars': 4.4},
                                                     'prime': False,
                                                     'sponsored': False},
        {'asin': 'B0824CTTQ7',
         'title': 'Pixel 4 - Clearly White - 64GB - Unlocked (Renewed)',
         'image': 'https://m.media-amazon.com/images/I/61D4hZNZ5jL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B0824CTTQ7/?psc=1',
         'prices': {'current_price': 241.0, 'previous_price': 418.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 452, 'stars': 4.3}, 'prime': False,
         'sponsored': False}, {'asin': 'B0175FR85W', 'title': 'Pixels',
                               'image': 'https://m.media-amazon.com/images/I/91xrsmHJ9cL._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B0175FR85W/?psc=1',
                               'prices': {'current_price': 2.99,
                                          'previous_price': -1.0,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 15791,
                                           'stars': 4.6}, 'prime': False,
                               'sponsored': False}, {'asin': 'B0766HPGYP',
                                                     'title': 'Google Pixel 2 128GB Unlocked GSM/CDMA 4G LTE Octa-Core Phone w/ 12.2MP Camera - Just Black',
                                                     'image': 'https://m.media-amazon.com/images/I/61v0enHOXpL._AC_UY218_.jpg',
                                                     'full_link': 'https://www.amazon.com/dp/B0766HPGYP/?psc=1',
                                                     'prices': {
                                                         'current_price': 130.99,
                                                         'previous_price': -1.0,
                                                         'currency': '$'},
                                                     'reviews': {
                                                         'total_reviews': 446,
                                                         'stars': 4.0},
                                                     'prime': False,
                                                     'sponsored': False},
        {'asin': 'B07KSSQQLZ',
         'title': 'Google - Pixel 3 with 64GB Memory Cell Phone (Unlocked) - Not Pink',
         'image': 'https://m.media-amazon.com/images/I/71krmniFaeL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B07KSSQQLZ/?psc=1',
         'prices': {'current_price': 219.95, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 617, 'stars': 4.3}, 'prime': False,
         'sponsored': False}, {'asin': 'B07R7DY911',
                               'title': 'Google - Pixel 3a with 64GB Memory Cell Phone (Unlocked) - Just Black',
                               'image': 'https://m.media-amazon.com/images/I/81T-FKC695L._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B07R7DY911/?psc=1',
                               'prices': {'current_price': 279.99,
                                          'previous_price': 399.0,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 8374,
                                           'stars': 4.4}, 'prime': False,
                               'sponsored': False}, {'asin': 'B095H15WLP',
                                                     'title': 'USB C Fast Charger, Wangmai 30W A&C Dual-Port Foldable PD Type c Charger, USB C Wall Charger Block for iPhone 13/12/11/Pro Max/XS/XR/X,iPad Pro, Pixel, Galaxy, and More',
                                                     'image': 'https://m.media-amazon.com/images/I/41d2GIVkmaL._AC_UY218_.jpg',
                                                     'full_link': 'https://www.amazon.com/dp/B095H15WLP/?psc=1',
                                                     'prices': {
                                                         'current_price': 13.99,
                                                         'previous_price': 23.99,
                                                         'currency': '$'},
                                                     'reviews': {
                                                         'total_reviews': 29,
                                                         'stars': 4.9},
                                                     'prime': False,
                                                     'sponsored': True},
        {'asin': 'B098V2B362',
         'title': 'Google Pixel 3 Unlocked Smartphone - 64GB Memory Cell Phone, Just Black, w/Charging Stand, Wired Earbuds and Google Charger - Bundle Set',
         'image': 'https://m.media-amazon.com/images/I/61YNb0vcezS._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B098V2B362/?psc=1',
         'prices': {'current_price': 225.0, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 37, 'stars': 4.0}, 'prime': False,
         'sponsored': False}, {'asin': 'B09DV93S9K',
                               'title': 'Google Pixel 5A 5G 128GB 6GB RAM Factory Unlocked (GSM Only | No CDMA - not Compatible with Verizon/Sprint) International Version - Black',
                               'image': 'https://m.media-amazon.com/images/I/51E7J1JKKXL._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B09DV93S9K/?psc=1',
                               'prices': {'current_price': 472.83,
                                          'previous_price': 515.0,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 49, 'stars': 4.2},
                               'prime': False, 'sponsored': False},
        {'asin': 'B0766TPHSH',
         'title': 'Google Pixel 2 XL 64GB Unlocked GSM/CDMA 4G LTE Octa-Core Smart Phone (Just Black)',
         'image': 'https://m.media-amazon.com/images/I/81dXcgzgqkL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B0766TPHSH/?psc=1',
         'prices': {'current_price': 154.99, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 216, 'stars': 4.4}, 'prime': False,
         'sponsored': False},
        {'asin': 'B01EGAMEC6', 'title': 'Pixels (4K UHD)',
         'image': 'https://m.media-amazon.com/images/I/914FRjkuyHL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B01EGAMEC6/?psc=1',
         'prices': {'current_price': 3.99, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 2272, 'stars': 4.7}, 'prime': False,
         'sponsored': False}, {'asin': 'B08KS4FKVP',
                               'title': 'Pixel C100 LED Continuous Output Video Light with Barn Door/4 Color Filters, 120W 5600K 98000lux CRI97+ TLCI99+ Photography Studio Light, Remote Controller for Portrait Shooting and Video Recording',
                               'image': 'https://m.media-amazon.com/images/I/71pBI4nky-L._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B08KS4FKVP/?psc=1',
                               'prices': {'current_price': 169.99,
                                          'previous_price': 269.99,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 10, 'stars': 4.4},
                               'prime': False, 'sponsored': True},
        {'asin': 'B08R61G69Q',
         'title': 'Google Pixel 4a with 5G - Android Phone - New Unlocked Smartphone with Night Sight and Ultrawide Lens - Just Black (Renewed)',
         'image': 'https://m.media-amazon.com/images/I/71DgN0WGe4L._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B08R61G69Q/?psc=1',
         'prices': {'current_price': 358.0, 'previous_price': 474.89,
                    'currency': '$'},
         'reviews': {'total_reviews': 123, 'stars': 4.2}, 'prime': False,
         'sponsored': False}, {'asin': 'B082YF9MMW',
                               'title': 'Unlocked Google Pixel 4 - 64GB - Just Black - GA01187-US (Renewed)',
                               'image': 'https://m.media-amazon.com/images/I/51Bch2bRtLL._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B082YF9MMW/?psc=1',
                               'prices': {'current_price': 244.99,
                                          'previous_price': 377.58,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 345, 'stars': 4.4},
                               'prime': False, 'sponsored': False},
        {'asin': 'B08MV7HWFK',
         'title': 'Unlocked Google Pixel 5 128GB Just Black GA01316-US (Renewed)',
         'image': 'https://m.media-amazon.com/images/I/81Uho2XBxQL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B08MV7HWFK/?psc=1',
         'prices': {'current_price': 429.0, 'previous_price': 960.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 190, 'stars': 4.0}, 'prime': False,
         'sponsored': False}, {'asin': 'B07KX8DXW8',
                               'title': 'Google Pixel 3 64GB Unlocked GSM & CDMA 4G LTE - Just Black (Renewed)',
                               'image': 'https://m.media-amazon.com/images/I/51YNSBaJ6oL._AC_UY218_.jpg',
                               'full_link': 'https://www.amazon.com/dp/B07KX8DXW8/?psc=1',
                               'prices': {'current_price': 150.99,
                                          'previous_price': -1.0,
                                          'currency': '$'},
                               'reviews': {'total_reviews': 248, 'stars': 4.0},
                               'prime': False, 'sponsored': False},
        {'asin': 'B09BQWHTQK',
         'title': 'Syncwire USB C Charger 30W Fast Wall Charger GaN II Mini Power Adapter PD Charger for iPhone 13 Pro Max/iPhone 12 Pro Max, MacBook Air, iPad Pro,Galaxy S21/ S21+,Pixel 6 Pro/6(Cable not Included)',
         'image': 'https://m.media-amazon.com/images/I/41dJiKfatVL._AC_UY218_.jpg',
         'full_link': 'https://www.amazon.com/dp/B09BQWHTQK/?psc=1',
         'prices': {'current_price': 16.99, 'previous_price': -1.0,
                    'currency': '$'},
         'reviews': {'total_reviews': 181, 'stars': 4.6}, 'prime': False,
         'sponsored': True}, {'asin': 'B09KMQK8QY',
                              'title': 'Jusy Case for Google Pixel 6 Pro, Enhanced Grip Durable Light Shockproof Flexible TPU Rubber Protective Cover for Pixel 6 Pro (Red)',
                              'image': 'https://m.media-amazon.com/images/I/71CnNIF3FSL._AC_UY218_.jpg',
                              'full_link': 'https://www.amazon.com/dp/B09KMQK8QY/?psc=1',
                              'prices': {'current_price': 8.99,
                                         'previous_price': -1.0,
                                         'currency': '$'},
                              'reviews': {'total_reviews': 5, 'stars': 4.1},
                              'prime': False, 'sponsored': True}]}

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
