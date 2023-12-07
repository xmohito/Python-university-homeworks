class FoodItem:
    def __init__(self, name, expiration_date):
        self.name = name
        self.expiration_date = expiration_date

    def display_info(self):
        print(f"Food Item: {self.name}, Expiration Date: {self.expiration_date}")


class TemperatureController:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature
        print(f"Temperature set to {new_temperature} degrees Celsius.")

    def display_temperature(self):
        print(f"Current Temperature: {self.temperature} degrees Celsius")


class Refrigerator:
    def __init__(self, brand, model, initial_temperature):
        self.brand = brand
        self.model = model
        self.temperature_controller = TemperatureController(initial_temperature)
        self.contents = []

    def add_food_item(self, food_item):
        self.contents.append(food_item)
        print(f"{food_item.name} added to the refrigerator.")

    def display_contents(self):
        print(f"Refrigerator Contents:")
        for item in self.contents:
            item.display_info()

fridge = Refrigerator(brand="CoolTech", model="X100", initial_temperature=4)

food_item1 = FoodItem("Milk", expiration_date="2023-01-15")
food_item2 = FoodItem("Eggs", expiration_date="2023-01-20")

fridge.add_food_item(food_item1)
fridge.add_food_item(food_item2)

fridge.display_contents()
fridge.temperature_controller.display_temperature()
