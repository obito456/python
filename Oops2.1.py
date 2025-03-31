class Player:
    Name="Dhoni"
    def __init__(self):
        print("New player is added")
    def __str__(self):
        return f"Name : {self.Name}"

p1=Player()
print(p1)
