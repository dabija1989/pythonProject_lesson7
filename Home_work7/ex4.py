"""Scrieți un program care utilizează o buclă while pentru a verifica dacă un număr întreg pozitiv dat n este un număr
prim. Un număr prim este un număr întreg pozitiv mai mare decât 1 care nu are divizori pozitivi în afară de 1 și el
însuși. Programul ar trebui să afișeze dacă numărul este prim sau nu.
"""
# Solution
integer = int(input("Introduceti un numar pozitiv:\n"))
este_prim = 0
if integer > 1:
    este_prim = 1
    divisor = 2
    while divisor * divisor <= integer and este_prim:
        if integer % divisor == 0:
            este_prim = 0
        divisor += 1
if este_prim:
    print(f"Numarul {integer} este prim.")
else:
    print(f"Numarul {integer} nu este un numar prim.")
