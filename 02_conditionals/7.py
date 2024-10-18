# Problem: Customize a coffee order: "Small", 
# "Medium", "Large" with an option for 
# "Extra shot" of espresso.

order_size = input("Enter the size of coffee: ")
extra_shot = input("Enter yes or no to get extra shot: ")

if extra_shot=="yes":
    coffee = order_size+" coffee with an extra shot"
else:
    coffee = order_size+" coffee"
