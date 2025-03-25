class Image:
    def __init__(self):
        self.name="image1"
        self.format=".jpg"

pic1=Image()
print(pic1.name)
del pic1
print(pic1)
