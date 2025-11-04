# Tahia Fahrin Karim, 20/09/2025
# Simple menu incorporating 'Register', 'View accounts (Login required)' and 'Exit'

def register_user():
    print("=== Register New Account ===")

    while True:                                         # Loop asking for a username which is not duplicate
        username = input("Enter new username: ")
        f = open("accounts.txt", "r")
        for line in f:
            file_username = line.strip().split(",")[0]  #Remove extra spaces and split the string into a list. file_username will be assigned the usernames, passwords will be ignored
            if username == file_username:
                print("❌ Username already exists! Try another one")
                break
        else:                                           # This else runs only if username is not duplicate
            break                                       # username is unique, exit while loop

    while True:                                         # Loop asking for a password meeting requirements
        password = input("Enter new password (min 10 characters): ")
        if len(password) < 10:                          # password min length should be 10
            print("❌ Password must be at least 10 characters long.")
        else:
            break                                       # Exit loop when password is valid


    f = open("accounts.txt", "a")

    f.write(username +"," + password + "\n")            # Append new user to file accounts.txt
    print("✅ Account successfully created.")
    f.close()

def login_user():
    print("=== User Login ===")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    f = open("accounts.txt", "r")
    s = f.readlines()

    for line in s:                              # check each line for username and password
        file_username, file_password = line.strip().split(",")          # Remove extra spaces and split the string into a list ['file_username', 'file_password']
        if username == file_username and password == file_password:
            print("✅ Login successful.")
            return username                     # Return username on success

    print("❌ Login failed. Invalid username or password.")
    return None

def display_users():
    print("== List of users ==")

    f = open("accounts.txt", "r")               #Open file for reading
    s = f.readlines()                           # read all lines from the file
    usernames_list =[]                          #Create an empty list to store usernames

    for line in s:                              #check each line for username and password
        file_username, file_password = line.strip().split(",")  # Remove extra spaces and split the string into a list ['file_username', 'file_password']
        usernames_list.append(file_username)

    f.close()

    counter = 1
    for username in usernames_list:
        print(str(counter) + ". " + username)
        counter = counter + 1

def main_menu():
    while True:                                                 #Loop for showing the main menu until 'Exit' is chosen
        print("=== Main Menu ===")
        print("1. Register")
        print("2. View Accounts (Login Required)")
        print("3. Exit")

        try:
            choice = int(input("Enter your pick (1,2,3): "))    # Get user choose which function to run

            if choice == 1:                                     #Register a new user option
                register_user()
            elif choice == 2:                                   #View Accounts option after logging in
                if login_user():                                #Call login function and check if it returns a successful login
                    display_users()                             #If login is successful, display usernames
                else:
                    print("⚠️ Access Denied. Please try logging in again!")
            elif choice == 3:
                print("Exit")
                break                       #Only break while loop for valid choice 3
            else:
                print("Invalid choice Please enter only numbers 1, 2, or 3.")       # for any invalid choice
        except ValueError:
            print("Invalid Input. Please only enter numbers 1~3")  # for any invalid input other than integers

main_menu()