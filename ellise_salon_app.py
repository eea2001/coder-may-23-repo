import sys
import datetime

colour_categories = {
    'light natural': ['light brown', 'blonde', 'white/grey', 'auburn'],
    'dark natural': ['mid to dark brown', 'black'],
    'vibrant': ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
}

def calculate_price(hair_type, hair_length, hair_thickness, hair_texture, hair_status, desired_service,
                    current_colour, desired_colour):
    base_price = 0
    sessions = 1
    total_hours = 1
    needs_bleaching = False

    if desired_service == 'colouring':
        base_price = 50
        if needs_bleaching == True: 
            base_price += 50
    elif desired_service == 'perm':
        base_price = 80


    # adjustments for price and hours based on: 
    
    # length 
    if hair_length == 'short':
        base_price += 10
        total_hours += 1
    elif hair_length == 'medium':
        base_price += 20
        total_hours += 2
    elif hair_length == 'long':
        base_price += 30
        total_hours += 3

    # thickness 
    if hair_thickness == 'thin':
        base_price += 5
        total_hours += 0.5
    elif hair_thickness == 'medium':
        base_price += 10
        total_hours += 1
    elif hair_thickness == 'thick':
        base_price += 15
        total_hours += 1.5
        
    # texture     
    if hair_texture == 'wavy':
        base_price += 5
        total_hours += 0.5
    elif hair_texture == 'curly':
        base_price += 10
        total_hours += 1
        
    # status 
    if hair_status == 'previously coloured':
        base_price += 20
        sessions += 1
        total_hours += 2
    elif hair_status== 'bleached':
        base_price += 30
        sessions += 2
        total_hours += 4
        
    # desired colour 
    if desired_service == 'colouring':
        if desired_colour != current_colour:
            if desired_colour in colour_categories['light natural']:
                base_price += 10
            elif desired_colour in colour_categories['dark natural']:
                base_price += 20
            elif desired_colour in colour_categories['vibrant']:
                base_price += 30
        
    return base_price, sessions, total_hours, needs_bleaching


# error handling 
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_options:
            return user_input.lower()
        else:
            print("Invalid input. Please enter a valid option.")
            
             
            
# HAIR COLOUR SELECT FUNCTION 
def select_hair_colour(category):
    colours = colour_categories.get(category)
    if colours:
        print(f"Please select a {category} hair colour:")
        counter = 1
        for colour in colours:
            print(f"{counter}. {colour}")
            counter += 1
        while True:
            try:
                index = int(input("Enter the number of your choice: ")) - 1
                if 0 <= index < len(colours):
                    return colours[index]
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# GENERATE QUOTE FUNCTION 
def generate_quote():
    desired_service = get_valid_input("Which service are you seeking a quote for? (Please enter 'colouring' or 'perm'): ", ['colouring', 'perm'])
    hair_length = get_valid_input("What is the length of your hair (short, medium, long)? ", ['short', 'medium', 'long'])
    hair_thickness = get_valid_input("What is the thickness of your hair (thin, medium, thick)? ", ['thin', 'medium', 'thick'])
    hair_texture = get_valid_input("What is the texture of your hair (straight, wavy, curly)? ", ['straight', 'wavy', 'curly'])
    hair_status = get_valid_input("What is the status of your hair? (natural, previously coloured, bleached): ", ['natural', 'previously coloured', 'bleached'])

    current_category = None
    desired_category = None
    current_colour = None
    desired_colour = None
    needs_bleaching = False
    hair_type = None 

    if desired_service == 'colouring':
        current_category = get_valid_input("Select your current hair colour category (light natural, dark natural, vibrant): ", ['light natural', 'dark natural', 'vibrant'])
        current_colour = select_hair_colour(current_category)
        if current_category == 'dark natural' or current_category == 'vibrant':
            needs_bleaching = True

        desired_category = get_valid_input("Select your desired hair color category (light natural, dark natural, vibrant): ", ['light natural', 'dark natural', 'vibrant'])
        desired_colour = select_hair_colour(desired_category)

    price, sessions, total_hours, _ = calculate_price(hair_type, hair_length, hair_thickness,
                                                                    hair_texture, hair_status, desired_service,
                                                                    current_colour, desired_colour)

    explanation = f"Based on the factors you provided:\n\n" \
                  f"Hair type: {hair_type}\n" \
                  f"Hair length: {hair_length}\n" \
                  f"Hair thickness: {hair_thickness}\n" \
                  f"Hair texture: {hair_texture}\n" \
                  f"Hair status: {hair_status}\n"

    if current_colour:
        explanation += f"Current hair colour: {current_colour}\n"
    if desired_colour:
        explanation += f"Desired hair colour: {desired_colour}\n"

    explanation += f"\nThe approximate price for {desired_service} is: ${price:.2f}.\n" \
                   f"Number of sessions: {sessions}\n" \
                   f"Total hours required: {total_hours:.1f}\n"

    if needs_bleaching:
        explanation += "\nYour hair type requires bleaching to achieve the desired color, " \
                       "which incurs an additional cost."

    return explanation




# loop for the whole program 
while True:
    quote = generate_quote()
    print(quote)

    response = input("Do you want to generate another quote? (y/n): ")
    if response.lower() != 'y':
        break

current_time = datetime.datetime.now()
print("Current Time:", current_time)

python_version = sys.version







# ___________TESTS___________

# ! HOW TO RUN THE TESTS !

# Perform the tests by running these functions and sections of the code
# Compare the actual output with the expected output for each test case
# Display the results of the tests


# Hair Colour Selection (Test 1)
# Purpose: to test the functionality of selecting hair colours from different categories.

# Test Case 1.1: Selecting a light natural hair colour
# Category: Light natural
# Input: Choose option 1 (light brown) from the list of colours.
# Expected Output: The selected colour should be "light brown".

# Test Case 1.2: Selecting a vibrant hair colour
# Category: Vibrant
# Input: Choose option 3 (yellow) from the list of colours.
# Expected Output: The selected colour should be "yellow".

# Price Calculation (Test 2)
# Feature Tested: The accuracy of price calculation based on various hair attributes and desired service.

# Test Case 2.1: Calculation for colouring service with medium length, thick hair, wavy texture, previously coloured status, and desired dark natural hair colour.
# Hair length: Medium
# Hair thickness: Thick
# Hair texture: Wavy
# Hair status: Previously coloured
# Desired service: Colouring
# Current colour: Blonde
# Desired colour: Mid to dark brown
# Expected Output: The calculated price should be $100, number of sessions should be 2, and total hours required should be 5.

# Test Case 2.2: Calculation for perm service with long length, thin hair, curly texture, natural status, and no desired colour.
# Hair length: Long
# Hair thickness: Thin
# Hair texture: Curly
# Hair status: Natural
# Desired service: Perm
# Expected Output: The calculated price should be $80, number of sessions should be 1, and total hours required should be 4.









