#zadanie 1
# Napisz program, który pyta użytkownika (input) o imię oraz wiek a następnie wyświetla napisy:
# Cześć <imię>!
# Twoje imię ma <liczba liter imienia> liter i zaczyna się od <pierwsza litera imienia>
# Teraz masz <wiek> lat, a za rok będzie to <wiek za rok>. Rok urodzenia to <rok urodzenia>
import datetime

def get_current_year():
    now = datetime.datetime.now()
    return now.year

def get_first_letter(name):
    if name:
        return name[0]
    return None

name = input("Enter your name: ")
age = input("Enter your age: ")
year = get_current_year()

if not name or not age.isdigit() or not age.isnumeric() or name.isdigit() or name.isspace() or int(age) > year:
    print("Something has gone wrong!")
else:
    age = int(age)
    birth_date = year - age
    next_year = age + 1

    print("Hi,", name)
    print("Your name has", len(name), "letters, and begins with", get_first_letter(name))
    print("Now, you're", age, "and next year you will be", next_year)
    print("Your year of birth is", birth_date)
