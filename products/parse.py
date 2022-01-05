from typing import Dict, List


class Product:
    def __init__(self, data: Dict, amount: float, validity: bool):
        self.data = data
        self.amount = amount
        self.validity = validity

    def get_product(self):
        five_products: List = []
        for product in self.data['results']:

            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices'],
                'image': product['image']
            }
            if (
                product_feature['price']['current_price'] > self.amount and
                self.validity
            ):
                five_products.append(product_feature)

            if len(five_products) >= 5:
                break

        return five_products

    def get_product_detail(self):
        five_products: List = []
        for product in self.data['results']:
            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices'],
                'image': product['image']
            }
            if (
                product_feature['price']['current_price'] > self.amount and
                self.validity
            ):
                five_products.append(product_feature)
            if (
                product_feature['price']['current_price'] == self.amount and
                self.validity
            ):
                five_products.append(product_feature)

            if len(five_products) >= 5:
                break

        return five_products
