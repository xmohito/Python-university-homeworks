class Character:
    def __init__(self, name, gender, lvl, attack_damage, health):
        self._name = name
        self._gender = gender
        self._lvl = lvl
        self._attack_damage = attack_damage
        self._health = health

    def take_damage(self, damage):
        self._health -= damage
        print(f'{self._name} took {damage} dmg. Health: {self._health}')

    def attack(self, target):
        print(f"{self._name} attacks {target._name} for {self._attack_damage} damage.")
        target.take_damage(self._attack_damage)

class Warrior(Character):
    def __init__(self, name, gender, lvl, attack_damage, health, weapon_type):
        super().__init__(name, gender, lvl , attack_damage, health)
        self._weapon_type = weapon_type

    def use_skill_1(self, target):
        skill_damage = self._attack_damage * 2
        print(f'{self._name} uses special skill on {target._name} for {skill_damage} dmg')
        target.take_damage(skill_damage)


player1 = Warrior(name='John', gender='male', lvl=23, attack_damage=18, health=300, weapon_type = 'Sword')
enemy1 = Character(name = 'Tony Sosa', gender='male', lvl=999, attack_damage=1000, health=999)

player1.attack(enemy1)
player1.use_skill_1(enemy1)