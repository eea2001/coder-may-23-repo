# define function that finds out whether the strong is palindrome or not

def is_palindrome(str):
   return str[::-1] == str

# input from the user
word = input("Enter your word: ")
# check user is palindrome or not
palindrome_check = is_palindrome(word)

# display output 
# if/else to print palindrome 

if palindrome_check: 
    print(f"{word} is a palindrome string")
else:
    print(f"{word} is not a palindrome string")

split function and len 
split to cut input into words 