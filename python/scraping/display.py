import os 
class display:
    def __init__(self, stats):
        self.stats = stats


    def print(self):
        print("""
            Hello from Covid Live

            - 7 day average is {stats.average_7d}
            - Active cases are {stats.active_case}
            - New Cases are {stats.percent_new_case} percent
            - Cases {stats.case_decreased}
        """)
    def clear_terminal(self):
        try: os.system('clear')
        except: 
            os.system('cls')
