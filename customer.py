
from shopping_cart import ShoppingCart

class Customer:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.customer_cart = ShoppingCart()
        

    def add_to_cart(self, new_item):
        self.customer_cart.new_product(new_item)
        


    def view_products(self):
        print("Here are the items currently in your cart:")
        for item in self.customer_cart.shopping_cart_list:
            print(item.product_name)
        

    
