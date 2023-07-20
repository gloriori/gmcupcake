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
        num_cakes = int(input('How many cupcakes would you like to create? (Cupcakes are $3.50 Each including frosting) '))
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

# let them pick by number

while True:
    flavour_input = input(
        'Pick the flavour you want!:\n 1) Chocolate $3.50 \n 2) Vanilla $3.50 \n 3) Red Velvet $3.50 \n 4) Carrot $3.50 \n '
        '5) Strawberry $3.50 \n 6) Lemon $3.50 \n 7) Confetti $3.50 \n \n[1/2/3/4/5/6/7]: ')

# Add individual messages for each input

    if flavour_input == '1':
        print('You picked: Chocolate\n')
        break
    elif flavour_input == '2':
        print('You picked: Vanilla\n')
        break
    elif flavour_input == '3':
        print('You picked: Red Velvet \n')
        break
    elif flavour_input == '4':
        print('You picked: Carrot \n')
        break
    elif flavour_input == '5':
        print('You picked: Strawberry \n')
        break
    elif flavour_input == '6':
        print('You picked: Lemon \n')
        break
    elif flavour_input == '7':
        print('You picked: Confetti \n')
        break

    else:
        print('Type a number 1-7')
        continue

print("Fantastic choice! \n")

# Give the user the icings

print("Here are the frostings/buttercreams we have available (Icing is included in the price of the cupcake flavouring) \n")

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

# let them pick by number

while True:
    icing_input = input(
        'Pick the Frosting you want!:\n 1) Strawberry Frosting \n '
        '2) Chocolate Frosting \n 3) Cream Cheese Frosting \n 4) Silky Swiss Meringue \n '
        '5) Whipped Cream Frosting \n 6) Vanilla Buttercream \n 7) Caramel Buttercream \n '
        '8) Lemon Buttercream \n \n[1/2/3/4/5/6/7/8]: ')

# Add individual messages for each input

    if icing_input == '1':
        print('You picked: Strawberry Frosting\n')
        break
    elif icing_input == '2':
        print('You picked: Chocolate Frosting \n')
        break
    elif icing_input == '3':
        print('You picked: Cream Cheese Frosting \n')
        break
    elif icing_input == '4':
        print('You picked: Silky Swiss Meringue\n')
        break
    elif icing_input == '5':
        print('You picked: Whipped Cream Frosting \n')
        break
    elif icing_input == '6':
        print('You picked: Vanilla Buttercream\n')
        break
    elif icing_input == '7':
        print('You picked: Caramel Buttercream\n')
        break
    elif icing_input == '8':
        print('You picked: Lemon Buttercream\n')
        break
    else:
        print('Type a number 1-8')
        continue

print("Perfect! \n")

# set the value for the toppings

num_toppings = num_cakes

# Give the user the topping options

print("Here are the toppings we have available (Topping will cost an extra 50c)")

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
# let them pick by number

while True:
    toppings_input = input(
        'Pick the Topping you want!:\n 1) Rainbow Sprinkles 50c \n '
        '2) Chocolate Sprinkles 50c \n 3) Chocolate Drizzle 50c \n 4) Caramel Drizzle 50c \n '
        '5) Sugar Pearls 50c  \n 6) Cherries 50c \n 7) Strawberries 50c  \n '
        '8) Marshmallows \n 9) None $0 \n \n[1/2/3/4/5/6/7/8/9]: ')


# Add individual messages for each input

    if toppings_input == '1':
        print('You picked: Rainbow Sprinkles \n')
        break
    elif toppings_input == '2':
        print('You picked: Chocolate Sprinkles \n')
        break
    elif toppings_input == '3':
        print('You picked: Chocolate Drizzle \n')
        break
    elif toppings_input == '4':
        print('You picked: Caramel Drizzle \n')
        break
    elif toppings_input == '5':
        print('You picked: Sugar Pearls \n')
        break
    elif toppings_input == '6':
        print('You picked: Cherries \n')
        break
    elif toppings_input == '7':
        print('You picked: Strawberries\n')
        break
    elif toppings_input == '8':
        print('You picked: Marshmallows\n')
        break
    elif toppings_input == '9':
        print('You picked: None \n')
        num_toppings = 0
        break
    else:
        print('Type a number 1-8')
        continue



# print out a message when the user chooses
print("Great choice!")
print("I will have", num_cakes, "cupcakes ready just for you!")

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

print(f"The total price of the cupcakes is: \n${cupcakes_cost}")
print("Thank you for purchasing our cupcakes!")
