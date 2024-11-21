import json

USERS_FILE = "users.json"
SCORES_FILE = "scores.json"

def load_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def register():
    users_data = load_file(USERS_FILE)
    full_name = input("Enter your full name: ")
    user_name = input("Choose a username: ")
    phone = input("Enter your phone number (must be 10 digits): ")
    if phone.isdigit() and len(phone) == 10:
        passwd = input("Set a password: ")
        enroll_no = input("Enter your enrollment number: ")
        if user_name in users_data:
            print("Username already exists. Please choose another one.")
        else:
            users_data[user_name] = {
                'name': full_name,
                'phone': phone,
                'password': passwd,
                'enrollment_no': enroll_no
            }
            save_file(USERS_FILE, users_data)
            print("Registration successful!")
    else:
        print("Invalid phone number. Please enter exactly 10 digits.")
        register()

def login():
    users_data = load_file(USERS_FILE)
    user_name = input("Enter your username: ")
    passwd = input("Enter your password: ")
    if user_name in users_data and users_data[user_name]['password'] == passwd:
        print(f"Welcome back, {users_data[user_name]['name']}!")
        return user_name
    else:
        print("Invalid username or password. Please try again.")
        return None

def quiz(user_name):
    quiz_questions = {
        'DSA': [
            {"question": "What is a stack?", "options": ["FIFO", "LIFO", "None"], "answer": 2},
            {"question": "What is a queue?", "options": ["FIFO", "LIFO", "None"], "answer": 1},
        ],
        'DBMS': [
            {"question": "What is SQL?", "options": ["Language", "Protocol", "None"], "answer": 1},
        ],
        'Python': [
            {"question": "What is Python?", "options": ["Snake", "Language", "IDE"], "answer": 2},
        ],
    }
    print("\nSelect a quiz category:\n1. DSA\n2. DBMS\n3. Python")
    choice = input("Enter your choice (1/2/3): ")
    category = {'1': 'DSA', '2': 'DBMS', '3': 'Python'}.get(choice)

    if not category:
        print("Invalid choice. Returning to main menu.")
        return

    points = 0
    for index, question in enumerate(quiz_questions[category], start=1):
        print(f"\nQ{index}: {question['question']}")
        for opt_index, option in enumerate(question['options'], start=1):
            print(f"{opt_index}. {option}")
        try:
            user_answer = int(input("Your answer (option number): "))
            if user_answer == question['answer']:
                points += 10
        except ValueError:
            print("Invalid input. Moving to the next question.")

    scores_data = load_file(SCORES_FILE)
    scores_data[user_name] = {'category': category, 'points': points}
    save_file(SCORES_FILE, scores_data)

    print(f"Quiz completed! Your score: {points}/50")

def view_scores(user_name):
    scores_data = load_file(SCORES_FILE)
    if user_name in scores_data:
        user_score = scores_data[user_name]
        print(f"\n--- Quiz Results ---\nCategory: {user_score['category']}\nScore: {user_score['points']}/50")
    else:
        print("No results found for your account. Please attempt a quiz first!")

def main():
    while True:
        print("\nMain Menu\n1. Register\n2. Login\n3. Exit")
        action = input("Select an option (1/2/3): ")

        if action == '1':
            register()
        elif action == '2':
            user_name = login()
            if user_name:
                while True:
                    print(f"\nHello, {user_name}! What would you like to do?")
                    print("1. Take a Quiz\n2. View Results\n3. Logout")
                    sub_action = input("Choose an option (1/2/3): ")

                    if sub_action == '1':
                        quiz(user_name)
                    elif sub_action == '2':
                        view_scores(user_name)
                    elif sub_action == '3':
                        print("You have been logged out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif action == '3':
            print("Thank you for using the Quiz App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
