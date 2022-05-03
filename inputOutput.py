start_form = "n"
start_form = input("Please press 'y' to start the form: ")

if start_form == "y":
    print("This is a short survey: ")
    user_first_name = input("first name:  ")
    user_last_name = input("last name:  ")
    user_age = 0
    try:
        user_age = int(input("Age: "))
    except ValueError:
        while type(user_age) != int:
            print("Error: Your input ist not a number")
            user_age = int(input("Age(please enter a number): "))

    user_jobtitle = input("Job Title: ")
    user_hobbies = list(input("Your hobbies: "))
    next_form_step = input("Press y to continue or n to exit")

    if next_form_step == "y":
        pass
    else:
        print("Your input: \n")
        print(f"Your name is {user_first_name} {user_last_name}.")
        print(f"You are {user_age} years old. Your job title is {user_jobtitle}")
        print("Your hobbies are:")
        for hobby in user_hobbies:
            print(hobby)
else:
    print("No forminput provided")
