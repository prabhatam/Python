#Problem: Suggest an activity based on the weather (e.g., sunny - go for a walk, rainy - read a book, snowy-build a snowman).
weather = input("Enter the weather condition: ")
weather=weather.lower()

if weather=="sunny":
    print("Go for a walk")
elif weather=="rainy":
    print("Read a book")
elif weather == "snowy":
    print("Make a snowman")
else:
    print("Enter a different weather condition")