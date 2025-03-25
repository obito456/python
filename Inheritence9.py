class Hacker:
    name="Anonymous"
    @classmethod
    def setname(self,name):
        self.name=name
    
hk1=Hacker()
hk1.setname("Dark king")
print(hk1.name)
print(Hacker.name)
