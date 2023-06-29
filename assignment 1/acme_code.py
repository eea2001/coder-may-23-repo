# create a dictionary for the skill weighting 
weighting = {
    'Python': 1,
    'Ruby': 2,
    'Bash': 4,
    'Git': 8,
    'HTML': 16,
    'TDD': 32,
    'CSS': 64,
    'JavaScript': 128
}
# therefore, the highest score a user could have is 255 

# to do next:
# user input the names of the program 
# return and print their raw score 


# function that calculates the raw score
def calculate_score (program_name):
    coding_skill_score = sum(weighting[competency]for competency in program_name if competency in weighting )
    return coding_skill_score

# asks for user input for the programs they are competent in 
program_names = []
while True:
    program_name = input ("Enter a skill, or please enter 0 to finish: " )
    if program_name == 0 :
        break 
    program_name.append(program_name)
    

user_score = calculate_score(program_name)

print(f"You coding skill score is {user_score}")
    







# def calculate_score (program_name), program_name is a key from weighting dict 
# need to make this .lower() so that user can input any case 
# print certain statements if their coding_skill_score == 255
# if coding_skill_score == 255: print("You have all the compentencies required for this role. We encourage you to apply! ")
# elif coding_skill_score >= 

def calculate_score (program_name):
    coding_skill_score = sum(weighting[competency]for competency in program_name if competency in weighting )
    return coding_skill_score




    
    

