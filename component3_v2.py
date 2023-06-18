# Ask the user how many cupcakes they would like to chose

while True:
    try:
        num_cakes = int(input('How many cupcakes would you like to create? '))
        print("Okay!", num_cakes, "cupcakes coming right up, but first lets choose a cupcake flavour")
        break
    except ValueError:
        print('Please enter a number.')


# set the value for the cupcake flavours

num_flavours = num_cakes

# Give the user the cupcake flavours

print("Here are the flavours that we have available!")

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

# turn the initial list into a numbered list

for index, item in enumerate(flavour_options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '

while user_flavour.lower() not in flavour_options:
    user_flavour = input(input_message)

# print out a message when the user chooses

print('You picked: ' + user_flavour)
print("What a fantastic choice!")

# set the value for the cupcake icing

num_icing = num_cakes

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

input_message = "Pick the flavour you want!:\n"

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

input_message = "Pick the flavour you want!:\n"

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
