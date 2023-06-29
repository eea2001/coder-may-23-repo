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

def calculate_score (program_names):
    coding_skill_score = sum(weighting[competency]for competency in program_names if competency in weighting )
    return coding_skill_score

program_names = []
while True: 
    program_name = input ("Enter a skill, or please enter 'X' to finish: " )
    if program_name == 'X' :
        break 
    elif program_name:
     program_names.append(program_name)
     
     
# while what is True though???
    
user_score = calculate_score(program_names)

print(f"You coding skill score is {user_score}") 