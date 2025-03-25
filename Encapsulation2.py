class Insta:
    def __init__(self,user,password):
        self.user=user
        self.__password=password
        self._access=False
    def getpassword(self):
        return self.__password
    def setaccess(self,access):
        self._access=access

user1=Insta("vj_rider","xyz")
print(user1.user)
print(user1.getpassword())
user1.setaccess(True)
print(user1._access)
