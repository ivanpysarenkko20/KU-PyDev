# Lab 04 – Zadanie 1 (★): Średnia ocen
#
# Program wczytuje oceny (float), każdą w osobnej linii, aż użytkownik
# wciśnie Enter w pustej linii. Potem wypisuje średnią z 2 miejscami, np.:
#     Średnia ocen: 4.00
# Jeśli nie podano żadnej oceny, wypisz: Brak ocen
#
# Wskazówki:
#   - pętla while True + break, gdy linia jest pusta
#   - licz sumę i liczbę ocen w dwóch zmiennych

# TODO: Twój kod poniżej

suma = 0
liczba_ocen = 0

while True:
    ocena = input("Podaj ocenę (lub wciśnij Enter, aby zakończyć): ")
    if ocena == "":
        break
    try:
        ocena_float = float(ocena)
        suma += ocena_float
        liczba_ocen += 1
    except ValueError:
        print("Nieprawidłowa ocena. Spróbuj ponownie.")

if liczba_ocen > 0:
    srednia = suma / liczba_ocen
    print(f"Średnia ocen: {srednia:.2f}")
else:
    print("Brak ocen")