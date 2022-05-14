
class ShoppingCart:

    def __init__(self):
        self.shopping_cart_list = []
        

    
    def total_in_cart(self):
        total = 0

        for item in self.shopping_cart_list:
            total += item.price
        return total

    
    def new_product(self, new_item):
        self.new_item = new_item
        self.shopping_cart_list.append(self.new_item)
        
    
    
    def empty_cart(self):
        self.shopping_cart_list = []
        return self.shopping_cart_list

        


        
       
     
