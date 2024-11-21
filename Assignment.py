print("""
    1 ----> Register
    2 ----> Log In
    3 ----> Recover Password
    4 ----> Exit
""")

users = []
user_data = {}
current_user = None

while True:
    choice = input("Please select a service by entering its number: ")
    
    if choice == '1':
        # Registration
        name = input("Enter your name: ").strip().lower()
        password = input("Create a password: ")
        date_of_birth = input("Enter your date of birth (format: 'dd/mm/yyyy') for password recovery: ")

        users.append(name)
        user_data[name] = {password: date_of_birth}

        print(f"Congratulations {name}, you have successfully registered!")

    elif choice == '2':
        # Login
        username = input("Enter your username: ").strip().lower()
        if username in users:
            entered_password = input("Enter your password: ")
            if entered_password in user_data[username]:
                print(f"Welcome back, {username}! You are logged in.")
                current_user = username
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please register first.")

    elif choice == '3':
        # Forgot Password
        if current_user is None:
            print("Please log in first to recover your password.")
        else:
            recovery_dob = input("Enter the date of birth you used during registration: ")
            if recovery_dob in user_data[current_user].values():
                new_password = input("Enter a new password: ")
                user_data[current_user] = {new_password: recovery_dob}
                print(f"Your password has been successfully updated, {current_user}!")
            else:
                print("Date of birth does not match our records. Please try again or register a new account.")

    elif choice == '4':
        print("Thank you for using our service. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid service.")
