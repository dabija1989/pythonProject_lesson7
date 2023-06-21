age = int(input("age\n"))
while age < 0:
    print("age can't be negative")
    age = int(input("age\n"))
print(f"Your age is {age}")