''' Bank Mod Simulation '''
#############################################################################################################

# Accounts Will Look Like This: #
# accounts[username] = [password, balance] #

#############################################################################################################
'''** ADMIN HELP **'''

# Admin Commands:
# 090 = Admin Menu on Main Menu #

#############################################################################################################

#def create_account(username, password, balance):
#    if username in accounts.keys():
#       print("Username Already Exists")
#       return False

accounts = dict()
user = ''

#############################################################################################################

import time
from time import sleep

#############################################################################################################

def login(username, password):
    if username in accounts.keys():
        if accounts[username][0] == password:
            print("Welcome, " + username)
            return True
        else:
            print("Incorrect Password")
            return False
    else:
        print("Username Not Found")
        return False

#############################################################################################################

print("WELCOME 2 SLxR.me. A Open Source Bank For SLxRIVNs.")
time.sleep(2.5)
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
   sleep(0.1)
   loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
   
#############################################################################################################

while user == 'q':
    print("Enter 0 to Create an Account.")
    print("Enter 1 to Deposit Money.")
    print("Enter 2 to Withdraw Money.")
    print("Enter 3 to Check Balance.")
    print ("Enter 4 to Login.")
    print("Enter 5 to Exit.")
    print("Enter 6 to Reset Password.")
    print("Enter 7 to Reset Username.")
    print("Enter 8 to Reset All.")
    print("enter 00 for Main Menu.")
    print("090 For Admin Menu.")
    print("080 For Help.")
    print("070 For Credits.")



user = input("Enter 00 to View Menu: ")

if user == '0':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    accounts[username] = [password, 0]
    print("Account Created")
    print("Username: " + username)
    print("Password: " + password)
    print("Balance: $0")
    print("Would You Like to Save This Account? (y/n)")
    save = input("Enter Your Choice: ")
    if save == 'y':
        with open('accounts.txt', 'a') as f:
            f.write(username + '\n')
            f.write(password + '\n')
            f.write(str(0) + '\n')
        print("Account Saved")
    print("")
    user = input("Deposit More or Enter 00 For Main Menu: ")
elif user == '1':
    print("Deposit Money")
    print("Please Login")
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        deposit = float(input("Enter Amount to Deposit: "))
        accounts[username][1] += deposit
        print("Deposit Successful")
        print("Balance: $" + str(accounts[username][1]))
        print("")
        user = input("Enter Your Choice: ")
elif user == '2':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        withdraw = int(input("Enter Amount to Withdraw: "))
        if withdraw > accounts[username][1]:
            print("Insufficient Funds")
            print("Balance: $" + str(accounts[username][1]))
            print("")
            user = input("Enter Your Choice: ")
elif user == '3':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        print("Balance: $" + str(accounts[username][1]))
        print("")
        user = input("Enter Your Choice: ")
elif user == '4':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        print("Welcome, " + username)
        print("")
        user = input("Enter Your Choice: ")
elif user == '5':
    print("Exiting")
    print("")
    user = input("Enter Your Choice: ")
elif user == '6':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        new_password = input("Enter Your New Password: ")
        accounts[username][0] = new_password
        print("Password Changed")
        print("")
        user = input("Enter Your Choice: ")
elif user == '7':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        new_username = input("Enter Your New Username: ")
        accounts[new_username] = accounts[username]
        del accounts[username]
        print("Username Changed")
        print("")
        user = input("Enter Your Choice: ")
elif user == '8':
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if login(username, password):
        accounts.clear()
        print("Accounts Cleared")
        print("")
        user = input("Enter Your Choice: ")
elif user == '00':
    print("Welcome to the Main Menu")
    user = input(" Enter a Menu Option: ")
    print("Enter 0 to Create an Account.")
    print("Enter 1 to Deposit Money.")
    print("Enter 2 to Withdraw Money.")
    print("Enter 3 to Check Balance.")
    print ("Enter 4 to Login.")
    print("Enter 5 to Exit.")
    print("Enter 6 to Reset Password.")
    print("Enter 7 to Reset Username.")
    print("Enter 8 to Reset All.")
    print("Enter RR To Restart Menu.")
    print("090 For Admin Menu.")
    print("080 For Help.")
    print("070 For Credits.")
    
elif user == '090':
    print("Welcome to the Admin Menu")
    user = input("Log into The Admin Account : ")
    if user == 'admin':
        print("Welcome, Admin")
        user = input("What Would You Like To Do: ")
        if user == 'F':
            print("Reset All Accounts?: ")
            user = input("Enter Admin Password: ")
            if user == 'admin.password':
                accounts.clear()
                print("Accounts Cleared")
                print("")
                user = input("Enter Your Choice: ")
            else:
                print("Verify Password: ")
##
elif user == '080':
    print("Welcome to the Help Menu")
    user = input("Send Help Email to SLxRE?: ")
    if user == 'y':
        print("Compose New Email")
        print("Enter Your Email Address: ")
        email = input("Enter Your Email Address: ")
        print("Enter Message: ")
        message = input("Enter Message: ")
        print("Enter Your Password: ")
        password = input("Enter Your Password: ")
        print("Sending Email...")
        sleep(2)
        def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filledLength = int(length * iteration // total)
            bar = fill * filledLength + '-' * (length - filledLength)
            print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
             # Print New Line on Complete
            if iteration == total:
                print()

        items = list(range(0, 50))
        l = len(items)

        loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
        for i, item in enumerate(items):
            sleep(0.1)
            loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
            print("Email Successfully Sent to SLxRE")
            sleep(2)
            print("Exit to Main Menu?: ")
            user = input("y/n: ")
            if user == 'y':
                print("Main Menu")
                user = input("Enter a Menu Option: ")
                print("Enter 0 to Create an Account.")
                sleep(1)
                print("Enter 1 to Deposit Money.")
                sleep(1)
                print("Enter 2 to Withdraw Money.")
                sleep(1)
                print("Enter 3 to Check Balance.")
                sleep(1)
                print ("Enter L to Logout.")
                sleep(1)
                print("Enter 4 to Login.")
                sleep(1)
                print("Enter 5 to Exit.")
                sleep(1)
                print("Enter 6 to Reset Password.")
                sleep(1)
                print("Enter 7 to Reset Username.")
                sleep(1)
                print("Enter 8 to Reset All.")
                sleep(1)
                print("enter RR To Restart Menu.")
                sleep(1)
                print("080 For Help.")
                sleep(1)
                print("070 For Credits.")
        


elif user == '5':
    print("Thank You For Using SLxRPvSS")
    user = 'q'


else:
    print("Invalid Input, Read Directions Carefully Then Try Again.")
        