class Hacker:
    name="Anonymous"
    def setname(self,name):
        self.name=name
    
hk1=Hacker()
hk1.setname("xavier")
print(hk1.name)
print(Hacker.name)
