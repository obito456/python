class Player:
    Team="India"
    def __init__(this,pname,Team):
        this.Name=pname
        this.Team=Team
    def score(self):
        print("Team scored 180 runs")
    @staticmethod
    def weather():
        print("the weather is sunny")

Player.weather()
print(Player.Team)
