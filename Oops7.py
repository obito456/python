class Player:
    Team="India"
    def __init__(this,pname,Team):
        this.Name=pname
        this.Team=Team
    def score(self):
        print("Team scored 180 runs")

p1=Player("ABD","South Africa")
print(p1.Team,p1.Name)
p2=Player("Virat","RCB")
print(p2.Team,p2.Name)
p1.score()
