from itertools import product
from product import Product


class ShoppingCart:

    def __init__(self):
        self.shopping_cart_list = [
            Product("soap",5, "hygiene"),
            Product("toothpaste",3, "hygiene"),
            Product("milk", 8 , "food")    
        ]

    
    def total_in_cart(self):
        total = 0
        for self.shopping_cart_list