class Theatre:
    Audience=0
    def __init__(self,Name,age):
        self.Name=Name
        self.age=age
        Theatre.Audience+=1

T1=Theatre("vijay",24);
T2=Theatre("geetha",21)
print(T1.Audience)
