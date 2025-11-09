# zadanie_1.py

#Funkcja wbudowana zip() ---
#Dok: https://docs.python.org/3/library/functions.html#zip
#Łączy elementy dwóch list w pary (krotki) element-po-elemencie

#Moduł standardowy math (użyjemy math.sqrt)
#Dok: https://docs.python.org/3/library/math.html
#math.sqrt(x) zwraca pierwiastek kwadratowy z x (dla x >= 0)

#Wyjątek ValueError
#Dok: https://docs.python.org/3/library/exceptions.html#ValueError
#Rzucany m.in. przez math.sqrt, gdy argument jest ujemny

import math

# 1) Dwie listy i łączenie zip()
temperatury_c=[12.5, 0.0, -3.2, 18.7]# przykładowe wartości (°C)
miasta=["Gdańsk", "Kraków", "Suwałki", "Wrocław"]

pary = list(zip(miasta, temperatury_c))
print("Pary (miasto, temp °C):", pary)
#Przykład: [("Gdańsk", 12.5)]

# 2) Użycie funkcji z math
wynik_poprw = math.sqrt(25)
print("sqrt(25) =",wynik_poprw)

# 3) Obsługa wyjątku try-except powodu sqrt(-1)
try:
    wynik_zle = math.sqrt(-1)  # wywoła ValueError
    print("sqrt(-1) =", wynik_zle)  # nie zostanie wykonane
except ValueError as e:
    print("ValueError przy sqrt(-1):", e)
