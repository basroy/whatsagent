from typing import Dict, List


class Products:
    def __init__(self, data: Dict, amount: int):
        self.data = data
        self.amount = amount

    def get(self) -> List:
        five_products: List = []
        for product in self.data['results']:

            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices']['current_price'],
                'image': product['image']
            }
            if (product_feature['price'] > -1.0 ):
                five_products.append(product_feature)

            if len(five_products) >= self.amount:
                break

        return five_products
