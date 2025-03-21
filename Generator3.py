def countdown():
    return 3
    return 2
    return 1

print(countdown())

def timer():
    yield 3
    yield 2
    yield 1

print(timer())
for i in timer():
    print(i)
