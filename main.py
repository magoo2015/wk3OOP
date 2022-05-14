from alarm_clock import AlarmClock
from product import Product
from customer import Customer


# clock_1 = AlarmClock()

# print(clock_1.alarm_time)
# clock_1.change_current_time("1000")

# alarm_setting = clock_1.alarm_on_or_off(False)
# print(alarm_setting)


first_cart = Customer("Sydney")

print(f"Customers name is:  {first_cart.customer_name}")

item_1 = Product("hammer", 30, "hardware")
item_2 = Product("eggs", 5, "food")
item_3 = Product("bleach", 3, "cleaning")
first_cart.add_to_cart(item_1)
first_cart.add_to_cart(item_2)
first_cart.add_to_cart(item_3)


first_cart.view_products()

total_price = first_cart.customer_cart.total_in_cart()

print(f"Here is the current total of your cart: ${total_price}")

first_cart.customer_cart.empty_cart()
first_cart.view_products()












