# Napisz programy, które pobierają od użytkowników odpowiednie liczby (input), a następnie wywołują funkcję, która obliczy:
#b) pierwiastki równania kwadratowego o parametrach a, b, c (tylko przypadki rzeczywiste):
#(algorytm opisany tutaj: https://www.matmana6.pl/rownanie-kwadratowe)
# Pamiętaj, że funkcje nie mają pobierać danych od użytkowników, a jedynie operować na podanych właściwie parametrach
# (czyli liczby mogą być również wpisane wcześniej w
# kodzie programu, należy też zadbać, aby do funkcji “nie dostało się” nic innego niż liczby).
# Oczywiście liczby nie muszą być całkowite.
#
# Wewnątrz funkcji należy zadbać, aby były
# spełnione odpowiednie warunki dotyczące wartości (np. niezerowość czy nieujemnosć liczb, nierówność trójkąta itp.).
# W definicjach funkcji na ogół nie powinny się znajdować operacje wypisania wartości (print),
# a jedynie obliczenia. Funkcje mają zwracać ostateczny wynik (o ile podano parametry, które pozwalają na jego obliczenie, w przeciwnym
# wypadku należy nic nie zwracać lub zwrócić wartość -1 - która często w podobnych programach oznacza,
# że “coś poszło nie tak”), a dopiero wynik przypisany do jakiejś zmiennej
# powinno się printować.
import math
def quadratic_function(a, b, c):
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return round(x1, 4), round(x2, 4)
        elif delta == 0:
            x1 = -b / (2 * a)
            return round(x1, 4)
        else:
            return -1
    else:
        return 0


a_str = input("Enter a:")
b_str = input("Enter b:")
c_str = input("Enter c:")

try:
    a = float(a_str)
    b = float(b_str)
    c = float(c_str)
except ValueError:
    print("Values must be numbers.")
    exit()

result = quadratic_function(a, b, c)

if result == -1:
    print("There is no solution.")
elif result == 0:
    print("A != 0")
else:
    print("The roots of the quadratic equation are:", result)