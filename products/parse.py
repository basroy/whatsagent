from typing import Dict, List


class Product:
    def __init__(self, data: Dict, amount: float, ):
        self.data = data
        self.amount = amount

    def get_product(self):
        five_products: List = []
        for product in self.data['results']:

            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices'],
                'image': product['image']
            }
            if product_feature['price']['current_price'] > -1.0:
                five_products.append(product_feature)

            if len(five_products) >= 5:
                break

        return five_products
