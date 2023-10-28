#zadanie2
# Zapytaj użytkownika o wiek oraz ilość pieniędzy w portfelu. Następnie dokonaj sprawdzenia, czy użytkownik może kupić w sklepie alkohol o wartości 20 zł. Rozpatrz wszystkie 4
# przypadki, z których tylko jeden spełnia warunek “jesteś pełnoletni i masz wystarczającą ilość pieniędzy”. Wyświetl stosowną informację dla każdego z przypadków, podając też
# informację, ile brakuje (w portfelu oraz do pełnoletniości).

money_amount_str = input ("Enter money amount: ")
age_str = input("Enter your age: ")

money_amount = None
age = None


if money_amount_str.isdigit() and age_str.isdigit() and int(money_amount_str) > 0 and int(age_str) > 0:
        money_amount = int(money_amount_str)
        age = int(age_str)
else:
    print("Incorrect inputs!")
    exit()

age_of_majority = 18
alcohol_value = 20
insufficient_funds = alcohol_value - money_amount
missing_years = age_of_majority - age

if age >= age_of_majority:
    if money_amount >= 20:
        print("You can buy an alcohol legally and have enough money.")
    elif money_amount < 20:
        print("You can buy an alcohol legally, but you don't have enough money.")
        print("Missing funds:", str(insufficient_funds) + ".")

else:
    if money_amount >= 20:
        print("You can't buy alcohol legally, but you have enough money.")
        print("You are", missing_years, "year(s) short of being able to legally buy alcohol.")

    elif money_amount < 20:
        print("You can't buy alcohol legally and you don't have enough money.")
        print("You are", missing_years, "year(s) short of being able to legally buy alcohol.")
        print("Missing funds:", str(insufficient_funds) + ".")