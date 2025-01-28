
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

    def Show(self): # We should pass the object to the class functions.  slef do this.
        print(f" The address is {self.add} and {self.pelak} and {Appartment.house}")

bahram = Appartment()
bahram.add = "ahwaz"
bahram.pelak = "45"
bahram.Show()

print(bahram.__dict__)
print(Appartment.__dict__)