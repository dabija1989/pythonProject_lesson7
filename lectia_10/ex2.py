"""
Create a program that will register a list of guests and food for a restaurant.

The user has to input how many guests will be coming

To register each guest, the user will input the name of the guest and two (2) dishes.

At the end, print out the list of the guests and what they ordered. And the total number of each dish the restaurant will have to prepare.

Use dict
Example:

Input:
3

Marius
Ravioli
Caesar Salad

Ana
Pepper steak
Caesar Salad

Gheorghe
Greek salad
Lentil Soup

Output:
The guests will be: [Marius, Ana, Gheorghe]
Output:
Marius ordered Ravioli and Caesar Salad
Ana ordered Pepper steak and Caesar Salad
Gheorghe ordered Greek salad and Lentil Soup
Output:
You will have to prepare:
Ravioli x 1
Caesar Salad x 2
Pepper steak x 1
Greek salad x 1
Lentil Soup x 1
"""
# Solution
num_guests = int(input("How many guests will be coming?\n"))
guests = {}

for _ in range(num_guests):
    guest_name = input("Enter guest name:\n")
    dish1 = input("Enter the first dish:\n")
    dish2 = input("Enter the second dish:\n")
    guests[guest_name] = {"dishes": [dish1, dish2]}

print("The guests will be:", list(guests.keys()))

print("\n")
for guest, order in guests.items():
    print(f"{guest} ordered {order['dishes'][0]} and {order['dishes'][1]}")

dish_counts = {}

for order in guests.values():
    for dish in order["dishes"]:
        dish_counts[dish] = dish_counts.get(dish, 0) + 1

print("\nYou will have to prepare:")
for dish, count in dish_counts.items():
    print(f"{dish} x {count}")




