# TypeError
# Won't run because it's trying to add an integer and a string
# def add_numbers(a, b):
#     result = a + b
#     print(f"The result is: {result}")

# # Example usage
# add_numbers(5, "10")

# Handle exception the above code outputs and produce a more useful output:
# wrap in a try block - 
def add_numbers(a, b):
    try:
        result = a + b
        print(f"The result is: {result}")
    except TypeError as e:
        print(f"Please provide two integers as arguments when invoking this function.")

# Example usage
add_numbers(5, "10")





#KeyError
# Occurs when you try to access a dictionary key that does not exist
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# def get_value(dictionary, key):
#      value = dictionary[key]
#      print(f"The value for '{key}' is: {value}")

# # Example usage
# get_value(my_dict, "name")
# get_value(my_dict, "occupation")

# Wrap the offending code in a try block
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
    except KeyError as e:
        print(f"KeyError: the key '{key}' was not found in the dictionary")

# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")





# ZeroDivisionError
# Occurs when you try to divide a number by zero  
# See shopping_cart.py for exercise 