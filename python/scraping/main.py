# Web Scraping 
# scrape the website 
# user which states 
# 7 day average 
# vaccination 
# active cases 
# percentage of new cases with respect to active cases 
# decrease or increase 

from user_input import UserInput 

if __name__ == "__main__":
    option = "c"
    while option == "c":
        # get state from user
        state = UserInput.get_state()
        print(state)
        
        
        #scrape website and get dictionary of website 
        
        # option to continue for next state 
        option = input("Enter 'c' to continue")
