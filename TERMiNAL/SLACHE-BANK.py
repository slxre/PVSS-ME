
'''Banking Stystem Using SLACHE OOP'''
                         
#############################################################################################################   

    # Parent Class : User 
        # Holds User Data
        # Holds User Account Data
        # Has a function to show user details
        # Has a function to show user account details
        # Has a function to show user account balance
        
#############################################################################################################
        
    # Child Class  : Bank
        # Has a function to create a new user
        # Has a function to show all users
        # Stores Data about the account balance of each user
        # Stores data about the amount of money in the bank, and for each user
        # Allows for deposits, withdrawals, transfers, view_balance, and view_account_balance, and view_all_account_balances
        # Has a function to show all users and their account balances
    
#############################################################################################################
    
    
class User():
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        
    def show_details(self):
        print("Username: " + self.username)
        print("Password: " + self.password)
        print("Balance: " + str(self.balance))
        
    def show_account_details(self):
        print("Username: " + self.username)
        print("Password: " + self.password)
        print("Balance: " + str(self.balance))
        
    def show_user_account_balance(self):
        print("Username: " + self.username)
        print("Password: " + self.password)
        print("Balance: " + str(self.balance))
    
    
    