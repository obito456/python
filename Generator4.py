import string

def letters():
    for x in string.ascii_lowercase:
        yield x
for let in letters():
    print(let)
