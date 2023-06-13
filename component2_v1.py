# ask user if about the program and if they have used it before

def program_user():
    new_user = input("Have you used this program before? ")
    if new_user == "":
        print("Sorry, but this cannot be blank. Please try again.")
        return program_user()
    elif new_user == 'yes' or new_user == 'Yes':
        print("Welcome back!")
    elif new_user == 'no' or new_user == 'No':
        print("Welcome to this program!")
    else:
        print("You must respond with Yes/No!")
        return program_user()


program_user()

#  ask the user if they want to read instructions


def rules_user():
    show_rules = input("Would you like to read the instructions? ")
    if show_rules == "":
        print("Sorry, but this cannot be blank. Please try again.")
        return rules_user()
    elif show_rules == 'yes' or show_rules == 'Yes':
        print('''\n 
                *** Instructions ***
    1st: Choose a cupcake flavour with the flavours that we have.
    2nd: Choose a icing that would like with the flavours that we have.
    3rd: Choose any toppings that would like to have with the options given''')
    elif show_rules == 'no' or show_rules == 'No':
        print("Okay, You may now start with building a cupcake!")
    else:
        print("You must respond with Yes/No!")
        return rules_user()


rules_user()