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

# Ask user what flavour they would like


def cupcake_flavour():
    cake_flavours = input("What cupcake flavour would you like to choose? ")
    if cake_flavours == "":
        print("Sorry this cannot be blank. Please try again.")
        return cupcake_flavour()
    elif cake_flavours == 'Vanilla' or cake_flavours == 'vanilla' or cake_flavours == 'Chocolate' or cake_flavours == 'Red Velvet' or cake_flavours == 'red velvet' or cake_flavours == 'Red velvet' or cake_flavours == 'red Velvet' or cake_flavours == 'Carrot Cake' or cake_flavours == 'carrot cake'  or cake_flavours == 'Carrot cake' or cake_flavours == 'carrot Cake' or cake_flavours == 'Strawberry' or cake_flavours == 'strawberry' or cake_flavours == 'lemon' or cake_flavours == 'Lemon' or cake_flavours == 'Coffee' or cake_flavours == 'coffee' or cake_flavours == 'confetti' or cake_flavours == 'Confetti':
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
    Please choose carefully and when you enter please enter' JUST the first word e.g Strawberry or Whipped
    ''')


# Ask user what flavour they would like


def frosting_flavour():
    frost_choice = input("What cupcake flavour would you like to choose? ")
    if frost_choice == "":
        print("Sorry this cannot be blank. Please try again.")
        return frosting_flavour()
    elif frost_choice == 'Strawberry' or frost_choice == 'strawberry' or frost_choice == 'Vanilla' or frost_choice == 'vanilla' or frost_choice == 'chocolate' or frost_choice == 'chocolate' or frost_choice == 'whipped' or frost_choice == 'Whipped' or frost_choice == 'caramel' or frost_choice == 'Caramel' or frost_choice == 'Silky' or frost_choice == 'silky' or frost_choice == 'cream' or frost_choice == 'Cream' or frost_choice == 'Lemon' or frost_choice == 'lemon':
        print("That is an amazing choice!")
    else:
        print("You may only enter options from the text above")
        return frosting_flavour()


frosting_flavour()

# Introduce toppings to user

print("Now that you have picked the frosting here are the toppings available!")
print('''\n 
                *** Toppings ***
    1. Rainbow Sprinkles
    2. Chocolate Sprinkles
    3. Cherries
    4. Sugar Pearls
    5. Marshmallows
    6. Strawberries
    7. Chocolate Drizzle
    8. Caramel Drizzle
    9. None
    \t
    Please enter the first word of the topping you want eg. Sugar or Rainbow! When it comes to Chocolate Sprinkles or 
    Chocolate Drizzle, enter it's full name!
    ''')

# ask the user what toppings they would like


def toppings_choice():
    top_choice = input("What topping would you like to choose? ")
    if top_choice == "":
        print("Sorry this cannot be blank. Please try again.")
        return toppings_choice()
    elif top_choice == 'None' or top_choice == 'none':
        print("That is okay, we may now calculate the final price of your cupcakes.")
    elif top_choice == 'Rainbow' or top_choice == 'rainbow' or top_choice == 'chocolate sprinkles' or top_choice == 'Chocolate Sprinkles' or top_choice == 'Chocolate sprinkles' or top_choice == 'chocolate Sprinkles' or top_choice == 'Cherries' or top_choice == 'cherries' or top_choice == 'Sugar' or top_choice == 'sugar' or top_choice == 'Marshmallows' or top_choice == 'marshmallows' or top_choice == 'strawberries' or top_choice == 'Strawberries' or top_choice == 'Chocolate Drizzle' or top_choice == 'chocolate drizzle' or top_choice == 'chocolate Drizzle' or top_choice == 'Chocolate drizzle' or top_choice == 'caramel' or top_choice == 'Caramel':
        print("That is a fantastic choice! We may now calculate the final price of your cupcakes.")
    else:
        print("You may only enter options from the text above")
        return toppings_choice()


toppings_choice()
