def calculate_rocket_fuel_required(distance_to_travel):
    answer = distance_to_travel * 15 
    if answer >= 100:
     return answer 
    elif answer < 100:
        return 100
        
     
print(calculate_rocket_fuel_required(10))
print(calculate_rocket_fuel_required(1))
print(calculate_rocket_fuel_required(20))





    