class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

class Electric(Car):
    def __init__(self, model, brand, range_per_charge):
        Car.__init__(self, model, brand)
        self.range_per_charge = range_per_charge

class Sport(Car):
    def __init__(self, model, brand, max_speed):
        Car.__init__(self, model, brand)
        self.max_speed = max_speed

class ElectricSports(Electric, Sport):
    def __init__(self, model, brand, range_per_charge, max_speed):
        Electric.__init__(self, model, brand, range_per_charge)
        Sport.__init__(self, model, brand, max_speed)

electric_sports_car = ElectricSports(model="ModelX", brand="Tesla", range_per_charge=300, max_speed=250)

print(f"Model: {electric_sports_car.model}")
print(f"Brand: {electric_sports_car.brand}")
print(f"Range per charge: {electric_sports_car.range_per_charge} km")
print(f"Max speed: {electric_sports_car.max_speed} km/h")




