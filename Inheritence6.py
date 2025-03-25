class Harikrishna:
    def __init__(self,role):
        self.role=role
    def surname(self):
        print("Nandamuri")
class NTR(Harikrishna):
    def __init__(self,industry):
        self.indusrty=industry
        super().surname()
ntr=NTR("TFI")
