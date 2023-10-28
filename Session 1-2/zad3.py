#zadanie3
# Napisz prosty kalkulator podatkowy dla podatku dochodowego. Najpierw program niech zapyta użytkownika, czy chce podać dochód miesięczny czy roczny. W przypadku wybrania
# dochodu miesięcznego oblicz dochód roczny. Następnie na podstawie podanych wartości oblicz wartość rocznego podatku dochodowego w oparciu o I i II próg podatkowy (12% i
# 32%) - sposób obliczania podatku według progów podatkowych znajdziesz w Internecie. Pomiń kwestie kwoty wolnej od podatku oraz założeń Polskiego Ładu

# 12% dla dochodów nieprzekraczających 120 000 zł,
# 32% dla nadwyżki ponad 120 000 zł.

income_period = input("Select:\n1 - monthly income\n2 - annual income\n Write option: ")

try:
    income_period = int(income_period)
    if income_period == 1:
        income_str = input("Enter your monthly income: ")
    elif income_period == 2:
        income_str = input("Enter your annual income: ")
    else:
        print("Invalid number.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

try:
    tax_threshold = 120000
    income = int(income_str)
    if income > 0:
        if income_period == 1:
            income = income * 12
            print("Annual income:", income)
        elif income_period == 2:
            income = income * 1
            print("Annual income:", income)

        if income <= tax_threshold:
            print("You are settled according to the 1st tax threshold.")
            taxable_amount = income / 1.12
            amount_tax = income - taxable_amount
            print("Annual income tax is:", round(amount_tax, 2))
        elif income > tax_threshold:
            print("You are settled according to the 2nd tax threshold.")
            surplus = income - tax_threshold
            print("Surplus:", surplus)
            taxable_amount = surplus / 1.32
            amount_tax = surplus - taxable_amount
            print("Annual income tax is:", round(amount_tax, 2))
        else:
            print("Invalid income period.")
    else:
        print("Income should be greater than 0.")
except ValueError:
    print("Invalid income amount. Please enter a valid number.")





