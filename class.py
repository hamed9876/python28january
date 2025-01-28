import datetime


class Human:

    def __init__(self,name,family):
        self.name = name
        self.family = family
        # print("This is human")

    def Show(self):
        print(f"the name is {self.name} and family is {self.family}")


jack = Human("jack", "jacki")
# jack.Show()


class Appartment:

    house = 4

    def __init__(self, name, pelak, age):
        self.name = name
        self.pelak = pelak
        self.age = age

    def Show(self): # We should pass the object to the class functions.  slef do this.
        print(f" The address is {self.name} and {self.pelak} and {self.age} and {Appartment.house}")

    @classmethod
    def getAge(cls,name,pelak,age):
        return cls(name,pelak,datetime.datetime.now().year - age)


# bahram = Appartment()
# bahram.add = "ahwaz"
# bahram.pelak = "45"
# bahram.Show()

# print(bahram.__dict__)
# print(Appartment.__dict__)

parastoo1 = Appartment.getAge("parastoo", 32, 2024)
parastoo1.Show()