



###############################################################################

user = input("Enter 00 to View Menu: ")

###############################################################################

###############################################################################

if user == '0':
    print("Enter Username:")
    username = input()
    print("Enter Password:")
    password = input()
    
    if login(username, password):
        print("Welcome, " + username)
        print("")
        user = input("Enter Your Choice: ")
    else:
        print("Invalid Username or Password")
        print("")
        user = input("Enter Your Choice: ")

###############################################################################

