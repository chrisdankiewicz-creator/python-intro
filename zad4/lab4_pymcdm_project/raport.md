# Laboratorium 4

## Cel
Celem było użycie biblioteki pymcdm do rozwiązania problemu wielokryterialnego podejmowania decyzji (MCDM) oraz porównanie metod TOPSIS i SPOTIS

## Dane
Zdefiniowano macierz decyzyjną (4 alternatywy, 3 kryteria):
C1 koszt – minimalizacja
C2 jakość – maksymalizacja
C3 czas – minimalizacja

Wagi kryteriów przyjęto ręcznie: [0.4, 0.4, 0.2]

Miejsce na zrzut ekranu:acierz danych / dane wejściowe

## Metody
TOPSIS uruchomiono na danych po normalizacji min-max (`minmax_normalization`).
SPOTIS uruchomiono na danych oryginalnych, definiując przedziały (bounds) dla kryteriów.

**Miejsce na zrzut ekranu: wyniki TOPSIS i SPOTIS z konsoli

## Wyniki i wnioski
TOPSIS wybiera alternatywę o największym wyniku, a SPOTIS o najmniejszym. Rankingi mogą się różnić, ponieważ metody inaczej mierzą „odległość od najlepszego rozwiązania”. Najlepsza alternatywa to ta, która stanowi najlepszy kompromis między kosztem, jakością i czasem.
