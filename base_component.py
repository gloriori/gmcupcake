# Introduce shop to user
print("Welcome to the Build a Cupcake Shop!")

# Get users name


def get_user():
    username = input("Please enter your name: ")
    if username == "":
        print("Sorry this can't be blank. Please try again.")
        return get_user()
    else:
        print(username + ", Welcome to Build a Cupcake!")


get_user()

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
    1. Select how many cupcakes you would like to make.
    2. Select a cupcake flavour with the flavours that we have.
    3. Select a icing that you would like with the flavours that we have.
    4. Select any toppings that you would like to have with the options given.
    5. We will give you the total price for your cupcakes.
    \t
    After that you are good to go to enjoy your cupcakes!
    ''')
    elif show_rules == 'no' or show_rules == 'No':
        print("Okay, You may now start building a cupcake!")
    else:
        print("You must respond with Yes/No!")
        return rules_user()


rules_user()
