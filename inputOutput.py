# start form input by pressing "y"
# add details for one or multiple users
# exit with "n" and display information

start_form = "n"
start_form = input("Please press 'y' to start the form input: ")
users = []
while start_form == "y":
    start_form = "n"
    user_first_name = input("first name:  ")
    user_last_name = input("last name:  ")
    user_gender = input("gender(m/w/x): ")
    try:
        user_age = int(input("Age: "))
    except ValueError:
        print("Error: Your input ist not a number")
        user_age = int(input("Age(please enter a number): "))

    user_jobtitle = input("Job Title: ")
    user_hobbies = input("Your hobbies: ")
    users.append({
        "first_name": user_first_name,
        "last_name": user_last_name,
        "gender": user_gender,
        "age": user_age,
        "job_title": user_jobtitle,
        "hobbies": user_hobbies
    })
    start_form = input("Press 'y' to add another user or 'n' to exit: ")
    if start_form == "n":
        for user in users:
            print(f"User Index: {users.index(user)}")
            print(f'full name: {user["first_name"]} {user["last_name"]}')
            print(f'gender and age: {user["gender"]} , {user["age"]}')
            print(f'Job title: {user["job_title"]}')
            print(f'Hobbies: {user["hobbies"]}')
            print("")
