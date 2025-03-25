class Virat:
    skills="Batting"
class Anushka:
    skills="Acting"
class Vamika(Virat,Anushka):
    pass
vamika=Vamika()
print(vamika.skills)
