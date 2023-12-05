class Turtle:
    def __init__(self, name, speed):
        # Check if name is a string
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")

        # Check if speed is at least 0
        if speed < 0:
            raise ValueError("Speed must be at least 0.")

        # Initialization: Initialize name and speed from the constructor, private field __x for position set to 0 by default
        self.name = name
        self.speed = speed
        self.__x = 0

    def say_name(self):
        # Print the turtle's name and speed
        print(f"My name is {self.name}. My speed is {self.speed}.")

    def move(self, distance):
        # Move the turtle by the specified distance
        self.__x += distance

    def get_position(self):
        # Get the current position of the turtle
        return self.__x


# Example usage with exception handling
try:
    turtle1 = Turtle('Turbo', 1)
    turtle1.say_name()

    turtle1.move(5)
    print(f"The current position of {turtle1.name} is: {turtle1.get_position()}.")
except ValueError as e:
    print(f"Error: {e}")
