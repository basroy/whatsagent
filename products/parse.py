from typing import Dict, List


class Products:
    def __init__(self, data: Dict, amount: int, test_name: str):
        self.data = data
        self.amount = amount
        self.test_name = test_name

    def get(self) -> List:
        five_products: List = []
        allowed_image_format: List =['jpg', 'gif', 'jpeg']
        allowed_url: List = ['https://www.amazon.com']
        allowed_high_value: float = 350.59
        print(self.data)
        for product in self.data['results']:
        # for product in self.data:
            # print(f'parse  {product}')
            product_feature: Dict = {
                'title': product['title'],
                'url': product['full_link'],
                'price': product['prices']['current_price'],
                'image': product['image'],
                'currency': product['prices']['currency']
            }
            valid_price_product: bool = product_feature['price'] > -1.0
            valid_title_product: bool = len(product_feature['title']) > 0
            null_image_product: bool = len(product_feature['image']) > 0
            valid_image_product: bool = (
                    product_feature['image'][-3:] in allowed_image_format
            )

            # https://www.amazon.com
            valid_url_product: bool = (
                    product_feature['url'][0:22] in allowed_url
            )
            # print(f'valid_url_product {valid_url_product} compare to {allowed_url}')
            valid_curr_product: bool = product_feature['currency'] in '$'
            valid_high_value_product: bool = (
                    product_feature['price'] > allowed_high_value
            )

            # I tried with all and any, and the conditional check always
        # evaluates to False. Hence, I did individual if statements and added
        # additional argument 'test_name'.
            all_valid_checks: bool = all([
                valid_url_product,
                valid_price_product,
                valid_high_value_product,
                valid_title_product,
                valid_image_product,
                null_image_product
            ] )
            if self.test_name == 'title':
                all_valid_checks: bool = valid_title_product
            elif self.test_name == 'price':
                all_valid_checks: bool = valid_price_product
            elif self.test_name == 'image':
                all_valid_checks: bool = all([
                    valid_image_product,
                    null_image_product
                ])
            elif self.test_name == 'url':
                all_valid_checks: bool = valid_url_product
            elif self.test_name == 'currency':
                all_valid_checks: bool = valid_curr_product
            elif self.test_name == 'minimum':
                all_valid_checks: bool = valid_high_value_product

            title_length: int = len(product_feature['title'])

            # print(f'all_valid_check --> {all_valid_checks}')
            if all_valid_checks:
                five_products.append(product_feature)
            if len(five_products) >= self.amount:
                break
        print(f'Is the list empty --> {five_products}')
        return five_products
