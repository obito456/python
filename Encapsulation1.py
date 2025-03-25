class Insta:
    def __init__(self,user,password):
        self.user=user
        self.__password=password
        self._access=False

user1=Insta("vj_rider","xyz")
print(user1.user)
print(user1.password)
print(user1.access)
