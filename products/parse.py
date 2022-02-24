from typing import Dict, List


class Products:
    def __init__(self, data: Dict, amount: int):
        self.data = data
        self.amount = amount


    def get(self) -> List:
        five_products: List = []
        allowed_image_format: List =['jpg', 'gif', 'jpeg']
        allowed_url: List = ['https://www.amazon.com']
        allowed_high_value: float = 350.59
        print(self.data)
        for product in self.data['results']:
            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices']['current_price'],
                'image': product['image'],
                'currency': product['prices']['currency']
            }
            all_valid_checks: bool = all ([
                product_feature['price'] > -1.0,
                len(product_feature['title']) > 0,
                len(product_feature['image']) > 0,
                product_feature['image'][-3:] in allowed_image_format,
                product_feature['url'][0:22] in allowed_url,
                product_feature['currency'] in '$',
                product_feature['price'] > allowed_high_value
            ])


            if all_valid_checks:
                five_products.append(product_feature)
            if len(five_products) >= self.amount:
                break
        return five_products
