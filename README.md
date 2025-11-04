# User-Login-Python-
This project is a beginner-friendly Python-based login system that simulates a basic user account manager using file handling. It’s designed to help new programmers understand how to build command-line authentication and registration systems without using databases.

🔧 Features:
User Registration (Component 1)
Users can create a new account by choosing a unique username and a password that is at least 10 characters long. The system prevents duplicate usernames by scanning the accounts.txt file before accepting new input.

Secure Login (Component 2)
Registered users must log in using their exact username and password. Credentials are validated against the saved data in accounts.txt. If login fails, the system displays an error and allows the user to try again until successful.

View Accounts (Component 3)
After a successful login, users are allowed to view a numbered list of all registered usernames. Passwords are never displayed, ensuring basic privacy.

User-Friendly Menu System
The application starts with a simple menu offering three options:
  - Register a new account
  - View existing users (login required)
  - Exit the program
  Input validation ensures users only select from options 1 to 3. Any other input results in a helpful error message.

🧠 Learning Outcomes:
This project demonstrates:
  - Use of local variables within functions
  - Input validation using try-except blocks
  - File handling (open, read, write) for persistent data storage
  - Control structures like loops and conditional statements
  - Basic user experience design for command-line apps

📁 Data Storage:
All account data is stored in a simple text file called accounts.txt, with each line formatted as: [username, password]

🚀 Future Improvements:
  - Mask password input using getpass
  - Add password strength validation
  - Allow users to change passwords or delete accounts
  - Use CSV or JSON for more structured data

This project is ideal for ICT beginners, or anyone learning Python basics.
