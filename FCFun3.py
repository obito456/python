def display(value):
    def product(x):
        return value*x
    return product

res=display(10)
print(res(3))
