age = int(input("Enter your age: "))
day = input("Enter current day: ")
price=12 if age>=18 else 8

if(day=="wednesday"):
    price=price-2

print("Ticket price for you is $",price)