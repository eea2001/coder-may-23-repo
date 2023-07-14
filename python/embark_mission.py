# have_supplies : boolean
# distance_to_mission_site : integer
# fuel_in_vehicle : integer

def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):

    if have_supplies == True and distance_to_mission_site <= 10:
     return True  
    
    elif have_supplies == True and fuel_in_vehicle >= distance_to_mission_site * 2:
     return True 

    else:
        return False 



print(ready_to_embark_on_mission(False, 1, 100)) # returns False

print(ready_to_embark_on_mission(True, 1, 100)) # returns True

print(ready_to_embark_on_mission(True, 5, 0)) # returns True

print(ready_to_embark_on_mission(True, 20, 30)) # returns False

print(ready_to_embark_on_mission(True, 20, 40)) # returns True

print(ready_to_embark_on_mission(True, 100, 300)) # returns True