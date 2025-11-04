FUNCTION login_user():

    username = ENTER username FROM user input
    password = ENTER password FROM user input

    OPEN file "items.txt" for reading
    READ all lines from file into variable s

    FOR each line in s:
        SPLIT line by comma into file_username and file_password
        REMOVE whitespace from both parts

        IF username = file_username AND password = file_password:
            PRINT "Login successful."
            RETURN username

    PRINT "Login failed. Invalid username or password."
    RETURN None


CALL login_user()