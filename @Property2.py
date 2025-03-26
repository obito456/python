class Wallet:
    def __init__(self,amount):
        self.__amount=amount
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,credit):
        self.__amount+=credit
w=Wallet(500)
w.amount=200
print(w.amount)
