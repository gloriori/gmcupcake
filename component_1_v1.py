# Introduce shop to user
print("Hello, welcome to Build a Cupcake!")


# Get users name


def get_user():
    username = input("Please enter your name: ")
    if username == "":
        print("Sorry this can't be blank. Please try again.")
        return get_user()
    else:
        print(username + ", Welcome to Build a Cupcake!")

        
get_user()
