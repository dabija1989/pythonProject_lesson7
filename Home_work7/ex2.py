"""Scrieți un program care generează un număr aleatoriu între 1 și 100 și permite utilizatorului să ghicească numărul.
Programul ar trebui să furnizeze feedback ("mai mare" sau "mai mic") până când utilizatorul ghicește numărul corect.
Programul ar trebui, de asemenea, să țină evidența numărului de încercări necesare pentru ca utilizatorul să ghicească
corect.
"""
# Solution
import random
numarul_aleatoriu = random.randint(1, 100)
num_incercari = 0
num_ghicit = 0
while num_ghicit != 1:
    numarul_introdus = int(input("Ghiceste un numar de la 1 la 100:\n"))
    num_incercari += 1

    if numarul_introdus < numarul_aleatoriu:
        print("Higher")
    elif numarul_introdus > numarul_aleatoriu:
        print("Lower")
    else:
        num_ghicit = 1
        print(f"Felicitari! Numarul cautat este {numarul_aleatoriu} la-i ghicit din {num_incercari} incercari.")


