tickets = int(input("How many tickets?"))

for i in range(0, tickets):
    age = int(input("Enter age: "))
    if age < 3:
        price = 0
    elif age >=3 and age < 12:
        price = 10
    else:
        price = 15
    print(f"Price for ticket is ${price}")