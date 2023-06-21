"""Scrieți un program care utilizează o buclă while pentru a calcula factorialul unui număr întreg pozitiv dat n.
Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
"""
# Solution
number = int(input("Introdu un numar intreg pozitiv:\n"))
if number < 0:
    print("numarul introdus nu este pozitiv")
    if number == 0:
        print(f"Factorial de {number} este 1.")
if number > 0:
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
print(f"Factorial din {number} este {factorial}.")