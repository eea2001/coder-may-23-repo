today_is_raining = input("Is it raining today? Type 'YES' or 'NO': ") # user input 
is_raining = True if today_is_raining == 'YES' else False # convert user input string to bool, any other input will make is_raining = False 

temp = float(input("What is the temperature today? ")) # define temp var as user input, convert string to float 

if is_raining == True and temp <= 15: 
 print("It's wet and cold :(")
elif is_raining == False and temp <= 15:
 print("It's not raining but it's cold!")
elif is_raining == False and temp >= 15:
 print("It's warm but not raining :)")
else:
 print("It's warm and raining !!!")
