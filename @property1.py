class Circle:
    def __init__(self,radius):
        self.__radius=radius
    @property
    def radius(self):
        return self.__radius
c1=Circle(2)
print(c1.radius)
