# set values for cupcake sections

price_flavour = 0.39
price_icing = 0.36
price_toppings = 0.14

# for testings ill make values for the nums

num_flavours = 4
num_icing = 4
num_toppings = 4

# calculate the flavour aka cupcake batter


def total_flavour_cost():
    flavours_cost = price_flavour * num_flavours
    return flavours_cost

# calculate the icing costs


def total_icing_cost():
    icing_cost = price_icing * num_icing
    return icing_cost

# calculate toppings cost


def total_toppings_cost():
    toppings_cost = price_toppings * num_toppings
    return toppings_cost


# calculate the final price


def total_cupcakes():
    cupcakes_cost = total_flavour_cost() + total_icing_cost() + total_toppings_cost()
    return cupcakes_cost


cupcakes_cost = total_cupcakes()

# print the price for the user to see

print(f"The total price of the cupcakes is: ${cupcakes_cost}")
