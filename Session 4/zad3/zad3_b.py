class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage.")
        target.receive_damage(self.damage)

    def receive_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def roar(self):
        print(f"{self.name} roars menacingly. Watch out!")


monster1 = Monster("Goblin", health=70, damage=10)
monster2 = Monster("Devil", health=10, damage=15)


monster1.roar()
monster1.attack(monster2)
