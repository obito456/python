class Player:
    Team="India"
    def __init__(this,pname):
        this.Name=pname

p1=Player("Rohit")
print(p1.Team,p1.Name)
p2=Player("Virat")
print(p2.Team,p2.Name)
print(Player.Team)
