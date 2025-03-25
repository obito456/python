class Harikrishna:
    def __init__(self,role):
        self.role=role
class NTR(Harikrishna):
    def __init__(self,industry,role):
        self.indusrty=industry
        super().__init__(role)
ntr=NTR("TFI","Actor")
print(ntr.role)
