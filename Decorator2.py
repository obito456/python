# YOU ORDERED AN ICECREAM WITH NUTS

def add_onion(fun):
    def wrapper():
        print("added onions 🧅")
        fun()
    return wrapper

def add_lemon(fun):
    def wrapper():
        print("added lemon 🍋")
        fun()
    return wrapper

@add_onion
@add_lemon
def get_Chicken():
    print("your Chicken is ready 🍗")

get_Chicken()
