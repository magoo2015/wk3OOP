from alarm_clock import AlarmClock
from product import Product
from customer import Customer
from shopping_cart import ShoppingCart

# clock_1 = AlarmClock()

# print(clock_1.alarm_time)
# clock_1.change_current_time("1000")

# alarm_setting = clock_1.alarm_on_or_off(False)
# print(alarm_setting)

# product_1 = Product("soap",5, "hygiene")
# product_2 = Product("toothpaste",3, "hygiene")
# product_3 = Product("milk", 8 , "food")

first_cart = ShoppingCart()


print(first_cart.shopping_cart_list[1].price)
total = first_cart.total_in_cart()
print(total)
first_cart.new_product(Product("hammer", 30, "hardware"))
total = first_cart.total_in_cart()
print(first_cart.total_in_cart())

current_list = first_cart.shopping_cart_list()
print(current_list)
first_cart.empty_cart()
print(first_cart.shopping_cart_list())



