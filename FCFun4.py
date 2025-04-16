def square(x):
    return x*x
fun=[square,lambda x:x+2,abs,max]
print(fun[0](4))
print(fun[1](4))
print(fun[2](-4))
print(fun[3](4,5))
