# Tahia Fahrin Karim, 20/09/2025
# Display numbered list of existing usernames only


def display_users():
    print("== List of users ==")

    f = open("accounts.txt", "r")             #Open file for reading
    s = f.readlines()                      # read all lines from the file
    usernames_list =[]                     #Create an empty list to store usernames

    for line in s:                         #check each line for username and password
        file_username, file_password = line.strip().split(",")  # Remove extra spaces and split the string into a list ['file_username', 'file_password']
        usernames_list.append(file_username)

    f.close()

    counter = 1
    for username in usernames_list:
        print(str(counter) + ". " + username)
        counter = counter + 1

display_users()


