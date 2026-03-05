# The following code generates a ZeroDivisionError
# shopping_cart_items = []

# def average_price(cart_items):
#     average = 0

#     for item in cart_items:
#       average += item.price

#     average = average / len(cart_items)

#     return average

# average_price_of_cart_items = average_price(shopping_cart_items)

# print(f"Your average cart item price is {shopping_cart_items} dollars")

# Task: have the function return 0 if there are no items in the cart by implementing a ty block 
shopping_cart_items = []

def average_price(cart_items):
  try:
      average = 0

      for item in cart_items:
        average += item.price

      average = average / len(cart_items)
      return average
  
  except ZeroDivisionError as e:
      return 0

# Call function 
average_price_of_cart_items = average_price(shopping_cart_items)
print(f"Your average cart item price is {average_price_of_cart_items} dollars")