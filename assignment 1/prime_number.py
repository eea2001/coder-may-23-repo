def is_prime (number):
    for i in range(2,number):
     if number % i == 0:
        return False 
    
    return True 

prime_numbers = []

for number in range(2,101):
    if is_prime(number):
        prime_numbers.append(number)

print(prime_numbers)



  

define 'is_prime' function that takes parameter 'number'

DEFINE is_prime with parameter 