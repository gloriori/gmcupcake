# set values for flavours plus toppings

price_cakes = 0.75

# set values for toppings

price_toppings = 0.14

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
