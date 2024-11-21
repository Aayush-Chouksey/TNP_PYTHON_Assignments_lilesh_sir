from questions import questions

user_records = {}  # Dictionary to store user data

def register_user():
    full_name = input("Enter your full name: ")
    user_name = input("Create a username: ")
    contact_number = input("Enter your 10-digit phone number: ")
    if len(contact_number) == 10:
        user_password = input("Set a password: ")
        roll_number = input("Enter your enrollment number: ")
        if user_name in user_records:
            print("Username already exists. Please try a different one.")
        else:
            user_records[user_name] = {
                'name': full_name,
                'phone': contact_number,
                'password': user_password,
                'enrollment': roll_number
            }
            print("Registration completed successfully!")
    else:
        print("Please enter a valid 10-digit phone number.")
        register_user()

def user_login():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if user_name in user_records and user_records[user_name]['password'] == user_password:
        print("Login successful!")
        return user_name
    else:
        print("Incorrect username or password. Please try again.")

def take_quiz(user_name):
    print("Available topics: 1. DSA 2. DBMS 3. Python")
    topic_choice = input("Select a topic by entering the number: ")

    if topic_choice == '1':
        topic = 'DSA'
    elif topic_choice == '2':
        topic = 'DBMS'
    elif topic_choice == '3':
        topic = 'Python'
    else:
        print("Invalid topic selection.")
        return

    score = 0
    for index, question in enumerate(questions[topic]):
        print(f"Q{index+1}: {question['question']}")
        for opt_index, option in enumerate(question['options']):
            print(f"{opt_index+1}. {option}")
        answer = int(input("Enter the correct option number: "))
        if answer == question['answer']:
            score += 10

    user_records[user_name]['score'] = score
    print(f"Quiz completed. Your score is {score}/50.")

def display_results(user_name):
    if 'score' in user_records[user_name]:
        print(f"""
        --------------------
        Name: {user_records[user_name]['name']}
        Enrollment Number: {user_records[user_name]['enrollment']}
        Quiz Score: {user_records[user_name]['score']}/50
        --------------------
        """)
    else:
        print("No quiz attempts found. Please attempt a quiz first.")

def main_menu():
    while True:
        print("\nMain Menu:\n1. Register\n2. Login\n3. Exit")
        user_choice = input("Select an option: ")

        if user_choice == '1':
            register_user()
        elif user_choice == '2':
            user_name = user_login()
            if user_name:
                while True:
                    print(f"\nWelcome, {user_name}!")
                    print("1. Take Quiz\n2. View Results\n3. Logout")
                    action_choice = input("Choose an action: ")

                    if action_choice == '1':
                        take_quiz(user_name)
                    elif action_choice == '2':
                        display_results(user_name)
                    elif action_choice == '3':
                        print("You have been logged out.")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif user_choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

main_menu()
