# parent class

class Chef:
    def __init__(self):
        pass

    def bake(self):
        pass

    def stir(self):
        pass

    def measure(self):
        pass


# child class

class PastryChef():
    def __init__(self):
        pass

    def bake(self):
        pass

    def stir(self):
        pass

    def measure(self):
        pass

    def knead(self):
        pass

    def whisk(self):
        pass


print("___________________________________________________")


class Animal():  # parent class
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):  # inheriting from Animal class
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()  # taking the breathe method from the Animal class
        print("doing this underwater.")  # additional attributes under the Fish class

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
# will print BOTH breathe methods -> inheritted from Animal class as well as the specified one from Fish class
