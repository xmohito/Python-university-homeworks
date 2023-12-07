class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


class Bird(Animal):
    def __init__(self, name, age, weight, color, wingspan, can_fly=True):
        super().__init__(name, age, weight)
        self.color = color
        self.wingspan = wingspan
        self.can_fly = can_fly

    def make_sound(self):
        print('Chirp chirp!')

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Weight: {self.weight} kg")
        print(f"Color: {self.color}")
        print(f"Wingspan: {self.wingspan} cm")
        print(f"Can fly: {self.can_fly}")

bird1 = Bird(name="Parrot", age=2, weight=0.1, color="Red", wingspan=15)
bird1.make_sound()
bird1.display_info()

bird2 = Bird(name="Penguin", age =1, weight=10, color="Black/white", wingspan=50, can_fly=False)
bird2.make_sound()
bird2.display_info()
