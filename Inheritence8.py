class Hacker:
    name="Anonymous"
    def setname(self,name):
        self.__class__.name=name
    
hk1=Hacker()
hk1.setname("Dark king")
print(hk1.name)
print(Hacker.name)
