# Napisz programy, które pobierają od użytkowników odpowiednie liczby (input), a następnie wywołują funkcję, która obliczy:
# a) pole trójkąta o bokach a,b,c
# (skorzystaj ze wzoru Herona: https://www.matmana6.pl/wzor-herona)
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
def triangle_area(a, b, c):
    # if all(isinstance(number, (int, float)) for number in (a, b, c)):
    if (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(s, 4)
    else:
        return -1


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

result = triangle_area(a, b, c)

if result == -1:
    print("The provided values do not form a valid triangle.")
else:
    print("The area of the triangle is equal to:", result)

