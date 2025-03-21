# YOU ORDERED AN ICECREAM WITH NUTS

def add_nuts(fun):
    def wrapper():
        print("added nuts 🥜")
        fun()
    return wrapper

@add_nuts
def get_icecream():
    print("your icecream is ready 🍦")

get_icecream()
