def multiply_two_numbers(num1, num2):
    return num1 * num2 

print(multiply_two_numbers(3,21))

# arguments are num1 and num2
# parameters act like local variables inside the body of a function, whatever we pass in as arguments take their place 

def subtract_two_numbers(num1, num2):
    return num1-num2

print(subtract_two_numbers(8,3))
print(subtract_two_numbers(3,8))

def print_greeting(greeting):
    print(greeting + "!!!")

print_greeting("Hello there")
print_greeting("Good evening")



# Optional parameter aka Default argument 

def print_greeting(greeting="hi"):
    print(greeting + "!!!")

print_greeting()
print_greeting("hey there")

# Using an equals sign like this is similar to using it to assign the value of a variable. 
# However any argument that we pass in to the function overwrites that default argument we set.




# Keyword Arguments 
# Allows us to ignore the order of arguments

def calculate_cost(price, shipping, tax_rate, member_discount): 
    return (price + (price * tax_rate)) + shipping - member_discount


print(calculate_cost(shipping=50, member_discount=20, price=200, tax_rate=0.2))
print(calculate_cost(tax_rate=0.2, member_discount=20, price=200,  shipping=50,))

# Combine strings

def combine_strings(string1, string2):
    return string1 + string2

new_string = combine_strings("Sal","ly")
print(new_string)




# Create a function called factor_check() that takes a non-negative integer as its argument. 
# The function should return True if the number is divisible by 3 or 5, and false otherwise.
def factor_check(num):
    if num == 0:
     return False
    if num % 3 == 0 or num % 5 == 0:
     return True 
    else: 
     return False 

result = factor_check(0)    
print(result)