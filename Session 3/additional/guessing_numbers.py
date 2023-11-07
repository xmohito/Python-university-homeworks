import random

attempts = 3

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

a = get_input("Enter the beginning of the range: ")
b = get_input("Enter the end of the range: ")

while (a + 2) > b:
    print("The end of the range must be greater, and the range must contain at least 3 numbers.")
    b = get_input("Enter the end of the range: ")

def is_numeric(guessed_number):
    return guessed_number.isnumeric()

numbers_list = list(range(a, b + 1))
print("Available numbers: ", numbers_list)

random_number = random.choice(numbers_list)

guessed_number = input("Guess a number: ")

while attempts > 0:
    if is_numeric(guessed_number):
        guessed_number = int(guessed_number)

        if guessed_number == random_number:
            print("You won!")
            exit()
        else:
            if attempts == 1:
                print("No more attempts, you lose!")
                print(f"The correct answer was: {random_number}")
                exit()
            else:
                if guessed_number > random_number:
                    print("The number is less than the given.")
                else:
                    print("The number is greater than the given.")
                attempts -= 1
                print(f"Attempts left: {attempts}")
                guessed_number = input("Guess a number: ")
    else:
        print("Value must be numeric!")
        guessed_number = input("Guess a number: ")

else:
    print("No more attempts, you lose!")
    print(f"The correct answer was: {random_number}")