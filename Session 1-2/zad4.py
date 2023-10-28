#zadanie4
# Zaprogramuj uproszczoną kasę fiskalną. Najpierw poproś użytkownika jednym wywołaniem input() o wpisanie produktów oddzielonych przecinkiem. Następnie dla każdego
# produktu (rozdziel je korzystając z funkcji poznanych dla stringów, a następnie stwórz z nich zbiór, aby zapewnić, że nie będą się powtarzać) poproś o wpisanie jego ceny i zapisz
# wszystko w postaci słownika. Na koniec wyświetl wszystkie elementy słownika w postaci “produkt:cena”.
def remove_spaces(input_string):
    return input_string.replace(" ", "")

while True:
    products_input = input("Enter products, separated by \",\": ")
    products_input = remove_spaces(products_input)

    if ',,' in products_input:
        print("Please do not use consecutive commas in your input.")
    else:
        break

product_list = products_input.split(",")

products_set = set()
for product in product_list:
    products_set.add(product)

products_dict = dict()
for product in products_set:
    print("Product:", product)
    while True:
        value = input("Enter price: ")
        try:
            value = float(value)
            if value > 0:
                value = round(value, 2)
                products_dict[product] = value
                break
            else:
                print("Price should be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
print("Products list:")
for product, price in products_dict.items():
    print(f"{product}:{price}")