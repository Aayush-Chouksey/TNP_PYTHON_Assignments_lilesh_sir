import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aayush@123",
    database="quiz_app"
)
cur = connection.cursor()

def register_user():
    full_name = input("Enter your full name: ")
    user_id = input("Enter a unique username: ")
    phone_number = input("Enter a valid 10-digit phone number: ")
    if len(phone_number) == 10:
        user_password = input("Create a secure password: ")
        roll_no = input("Enter your enrollment/roll number: ")

        cur.execute("SELECT * FROM users WHERE username = %s", (user_id,))
        if cur.fetchone():
            print("The username is already in use. Please try another.")
        else:
            cur.execute(
                "INSERT INTO users (name, username, phone_no, password, enrollment_no) VALUES (%s, %s, %s, %s, %s)",
                (full_name, user_id, phone_number, user_password, roll_no)
            )
            connection.commit()
            print("You have successfully registered!")
    else:
        print("Please provide a valid 10-digit phone number.")
        register_user()

def user_login():
    user_id = input("Enter your username: ")
    user_password = input("Enter your password: ")

    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user_id, user_password))
    if cur.fetchone():
        print("Welcome back! Login successful.")
        return user_id
    else:
        print("Incorrect username or password. Please try again.")

def take_quiz(user_id):
    print("Available quiz sections: 1. DSA 2. DBMS 3. Python")
    selected_section = input("Choose a section number to proceed: ")

    if selected_section == '1':
        selected_section = 'DSA'
    elif selected_section == '2':
        selected_section = 'DBMS'
    elif selected_section == '3':
        selected_section = 'Python'
    else:
        print("Invalid selection. Please choose a valid section.")
        return

    cur.execute("SELECT * FROM questions WHERE section = %s", (selected_section,))
    quiz_questions = cur.fetchall()

    if not quiz_questions:
        print("Sorry, no questions available in this section at the moment.")
        return

    total_score = 0
    for idx, question in enumerate(quiz_questions):
        print(f"Q{idx + 1}: {question[2]}")  
        print(f"1. {question[3]}")        
        print(f"2. {question[4]}")        
        print(f"3. {question[5]}")        
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer == question[6]:
            total_score += 10

    cur.execute(
        "INSERT INTO scores (username, section, score) VALUES (%s, %s, %s)",
        (user_id, selected_section, total_score)
    )
    connection.commit()

    print(f"Congratulations! You scored: {total_score}/50")

def view_results(user_id):
    cur.execute("SELECT section, score FROM scores WHERE username = %s", (user_id,))
    quiz_results = cur.fetchall()
    if quiz_results:
        for sec, scr in quiz_results:
            print(f"Section: {sec}, Your Score: {scr}/50")
    else:
        print("It seems you haven't taken any quiz yet.")

def menu():
    while True:
        print("\nMain Menu:\n1. Register\n2. Login\n3. Exit")
        menu_choice = input("Please select an option: ")

        if menu_choice == '1':
            register_user()
        elif menu_choice == '2':
            user_id = user_login()
            if user_id:
                while True:
                    print("\nYou are logged in as:", user_id)
                    print("1. Take Quiz\n2. View Results\n3. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        take_quiz(user_id)
                    elif option == '2':
                        view_results(user_id)
                    elif option == '3':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid selection. Please try again.")
        elif menu_choice == '3':
            print("Thank you for using the Quiz App. Goodbye!")
            connection.close()
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

menu()
