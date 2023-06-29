# set up dictionary for weightings 
weightings = {
    'Python': 1,
    'Ruby': 2,
    'Bash': 4,
    'Git': 8,
    'HTML': 16,
    'TDD': 32,
    'CSS': 64,
    'JavaScript': 128
}

# showing user the list of skills 
print("Skills required for the role:")
for skill_name in weightings.keys():
 print(skill_name)
print("Please note when entering a skill that program is case sensitive!")

# initialise empty list to store skills 
user_input_skills = []
# prompting user input 
skill = input("Enter a skill from above (or 'x' to finish): ")

# while the user has entered anything beside 'x', the list will add the skills until they enter 'x'
while skill !='x':
    user_input_skills.append(skill)
    skill = input("Enter another skill (or 'x') to finish: ")
       
# user_score must be 0 before loop
user_score = 0


# if the skill input byt user is one of the keys, its weight is added to user_score 
for skill in user_input_skills:
    if skill in weightings:
        user_score+=weightings[skill]   

# tells user their score         
print("Your coding skill score:", user_score)

# check with skills are dict keys that are NOT in user_input_skills and sum the those weightings to calculate missing_skills_score 
missing_skills_score = sum(weightings[skill] for skill in weightings.keys() if skill not in user_input_skills)

# print the list of missing skills
print("You are missing the following skills: ")
for skill in weightings.keys():
    if skill not in user_input_skills:
        print(skill)

# tell user what skills they're missing, and how much they can improve their score 
print("By learning these skills, you can improve your coding skill score by:", missing_skills_score, "!")






