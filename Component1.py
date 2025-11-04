# Tahia Fahrin Karim, 24/09/2025
# Register a new user with a username and a password

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

register_user()