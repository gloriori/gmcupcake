# Ask the user how many cupcakes they would like to chose
while True:
    try:
        num_cakes = int(input('How many cupcakes would you like to create? '))
        print("Okay!", num_cakes, "cupcakes coming right up, but first lets choose a cupcake flavour")
        break
    except ValueError:
        print('Please enter a number.')


# Give the user the cupcake flavours

print("Here are the flavours that we have available!")
print('''\n 
                *** Cupcake Flavours ***
    1. Chocolate
    2. Vanilla
    3. Red Velvet
    4. Carrot cake
    5. Strawberry
    6. Lemon
    7. Coffee
    8. Confetti
    \t
    Please choose carefully!
    ''')


# Set flavours in three lists

flavour_one = ['Vanilla', 'vanilla', 'Chocolate', 'chocolate', 'Red Velvet', 'red velvet', 'Red velvet', 'red Velvet']
flavour_two = ['Carrot Cake', 'carrot cake', 'carrot Cake', 'Carrot cake', 'Strawberry', 'strawberry', 'Lemon', 'lemon']
flavour_three = ['Coffee', 'coffee', 'Confetti', 'confetti']

# Ask user what flavour they would like


def cupcake_flavour():
    cake_flavours = input("What cupcake flavour would you like to choose? ")
    if cake_flavours == "":
        print("Sorry this cannot be blank. Please try again.")
        return cupcake_flavour()
    elif cake_flavours in flavour_one or flavour_two or flavour_three:
        print("I love that flavour too!")
    else:
        print("You may only enter options from the text above")
        return cupcake_flavour()


cupcake_flavour()

# Introduce frostings to user

print("Now that you have picked the flavour here are the frosting available!")
print('''\n 
                *** Frosting Flavours ***
    1. Strawberry Frosting
    2. Vanilla Buttercream
    3. Chocolate Frosting
    4. Whipped Cream Frosting
    5. Caramel Buttercream Frosting
    6. Silky Swiss Meringue Buttercream Frosting
    7. Cream Cheese Frosting
    8. Lemon Buttercream
    \t
    Please choose carefully and when you enter please enter' JUST the first word e.g Strawberry or Whipped!
    ''')

# Set frostings into lists

frosting_one = ['Strawberry', 'strawberry', 'Vanilla', 'vanilla', 'Chocolate', 'chocolate', 'Whipped', 'whipped']
frosting_two = ['Caramel', 'caramel', 'Silky', 'silky', 'Cream', 'cream', 'Lemon', 'lemon']

# Ask user what flavour they would like


def frosting_flavour():
    frost_choice = input("What cupcake flavour would you like to choose? ")
    if frost_choice == "":
        print("Sorry this cannot be blank. Please try again.")
        return frosting_flavour()
    elif frost_choice in flavour_one or flavour_two or flavour_three:
        print("That is an amazing choice!")
    else:
        print("You may only enter options from the text above")
        return frosting_flavour()


frosting_flavour()
