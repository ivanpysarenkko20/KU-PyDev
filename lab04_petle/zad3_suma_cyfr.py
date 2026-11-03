# Lab 04 – Zadanie 3 (★): Suma i liczba cyfr
#
# Program wczytuje nieujemną liczbę całkowitą i wypisuje DOKŁADNIE:
#     Suma cyfr: 15
#     Liczba cyfr: 5
# (dla 12345).
#
# Rozwiąż to ARYTMETYCZNIE pętlą while, bez zamiany na tekst:
#   - n % 10 to ostatnia cyfra,
#   - n // 10 „odcina” ostatnią cyfrę.
# Uwaga: liczba 0 ma jedną cyfrę.

# TODO: Twój kod poniżej

n = int(input("Wpisz nieujemną liczbę całkowitą: "))   

suma_cyfr = 0
liczba_cyfr = 0

while n > 0:
    ostatnia_cyfra = n % 10
    suma_cyfr += ostatnia_cyfra
    liczba_cyfr += 1
    n //= 10

if liczba_cyfr == 0: 
    liczba_cyfr = 1

print(f"Suma cyfr: {suma_cyfr}")
print(f"Liczba cyfr: {liczba_cyfr}")