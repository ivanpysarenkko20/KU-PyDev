# Lab 01 – Zadanie 4 (☆, dodatkowe): Kategoria BMI
#
# Rozbuduj kalkulator BMI: po obliczeniu wypisz także kategorię (wg WHO):
#     BMI < 18.5          -> niedowaga
#     18.5 <= BMI < 25    -> waga prawidłowa
#     25 <= BMI < 30      -> nadwaga
#     BMI >= 30           -> otyłość
#
# To zadanie wymaga instrukcji if / elif / else, którą dokładnie poznasz
# w labie 03. Spróbuj już teraz – składnię znajdziesz na slajdach.

# TODO: Twój kod poniżej
waga = float(input("Podaj wagę (w kg): "))
wzrost = float(input("Podaj wzrost (w metrach, np. 1.75): "))

bmi = waga / (wzrost ** 2)

print(f"Twoje BMI wynosi: {bmi:.2f}")

if bmi < 18.5:
    print("niedowaga")
elif 18.5 <= bmi < 25:
    print("waga prawidłowa")
elif 25 <= bmi < 30:
    print("nadwaga")
else:
    print("otyłość")
