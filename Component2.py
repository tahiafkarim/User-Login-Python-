# Tahia Fahrin Karim, 20/09/2025
# Check Login with a username and a valid password


def login_user():
    print("=== User Login ===")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    f = open("items.txt", "r")
    s = f.readlines()

    for line in s:                              # check each line for username and password
        file_username, file_password = line.strip().split(",")          # Remove extra spaces and split the string into a list ['file_username', 'file_password']
        if username == file_username and password == file_password:
            print("✅ Login successful.")
            return username                     # Return username on success

    print("❌ Login failed. Invalid username or password.")
    return None

login_user()

