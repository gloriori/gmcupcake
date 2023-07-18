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
    5. We will give you the total price for your cupcakes and a receipt if you would like one.
    
    \t
    After that you are good to go to enjoy your cupcakes!
    ''')
    elif show_rules == 'no' or show_rules == 'No':
        print("Okay, You may now start building a cupcake!")
    else:
        print("You must respond with Yes/No!")
        return rules_user()


rules_user()

# Ask the user how many cupcakes they would like to chose

while True:
    try:
        num_cakes = int(input('How many cupcakes would you like to create? '))
        print("Okay!", num_cakes, "cupcakes coming right up, but first lets choose a cupcake flavour \n ")
        break
    except ValueError:
        print('Please enter a number.')


# Give the user the cupcake flavours

print("Here are the flavours that we have available! \n")

# make the cupcake flavours into a list

flavour_options = ['chocolate',
                   'vanilla',
                   'red velvet',
                   'carrot',
                   'strawberry',
                   'lemon',
                   'coffee',
                   'confetti'
                   ]

user_flavour = ''

input_message = "Pick the flavour you want!:\n"

while True:
    user_input = input(
        'Pick the flavour you want!:\n \n 1) Chocolate \n 2) Vanilla \n 3) Red Velvet \n 4) Carrot \n 5) Strawberry '
        '\n 6) Lemon \n 7) Confetti \n \n[1/2/3/4/5/6/7]: ')

    if user_input == '1':
        print('Chocolate, what a fantastic choice!')
        break
    elif user_input == '2':
        print('Vanilla, what a fantastic choice!')
        break
    elif user_input == '3':
        print('Red Velvet, what a fantastic choice!')
        break
    elif user_input == '4':
        print('Carrot, what a fantastic choice!')
        break
    elif user_input == '5':
        print('Strawberry, what a fantastic choice!')
        break
    elif user_input == '6':
        print('Lemon, what a fantastic choice!')
        break
    elif user_input == '7':
        print('Confetti, what a fantastic choice!')
        break

    else:
        print('Type a number 1-7')
        continue


# Give the user the icings

print("Here are the frostings/butter creams we have available")

# make the icings into a list

icing_options = [
    'strawberry frosting',
    'chocolate frosting',
    'cream cheese frosting',
    'silky swiss meringue',
    'whipped cream frosting',
    'vanilla buttercream',
    'caramel buttercream',
    'lemon buttercream'
]

user_icing = ''

input_message = "Pick the frostings you want!:\n"

# turn the initial list into a numbered list

for index, item in enumerate(icing_options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '

while user_icing.lower() not in icing_options:
    user_icing = input(input_message)

# print out a message when the user chooses

print('You picked: ' + user_icing)
print("I love that icing too!")

# set the value for the toppings

num_toppings = num_cakes

# Give the user the topping options

print("Here are the toppings we have available")

# make the toppings into a list

toppings_options = ['rainbow sprinkles',
                    'chocolate sprinkles',
                    'chocolate drizzle',
                    'caramel drizzle',
                    'sugar pearls',
                    'cherries',
                    'strawberries',
                    'marshmallows',
                    'none'
                    ]

user_toppings = ''

input_message = "Pick the toppings you want!:\n"

# turn the initial list into a numbered list

for index, item in enumerate(toppings_options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '

while user_toppings.lower() not in toppings_options:
    user_toppings = input(input_message)

# if user chooses none set the number of toppings to 0

if user_toppings == 'none':
    num_toppings = 0

# print out a message when the user chooses

print('You picked: ' + user_toppings)
print("Great choice!")
print("I will have", num_cakes, user_flavour, "cupcakes ready just for you!")

# set values for flavours plus toppings

price_cakes = 3.50

# set values for toppings

price_toppings = 0.50

# calculate the flavour aka cupcake batter plus toppings


def total_cakes_cost():
    cakes_cost = price_cakes * num_cakes
    return cakes_cost


# calculate toppings cost


def total_toppings_cost():
    toppings_cost = price_toppings * num_toppings
    return toppings_cost


# calculate the final price

def total_cupcakes():
    cupcakes_cost = total_cakes_cost() + total_toppings_cost()
    return cupcakes_cost


cupcakes_cost = total_cupcakes()

# print the price for the user to see

print(f"The total price of the cupcakes is: ${cupcakes_cost}")
print("Thank you for purchasing our cupcakes!")
