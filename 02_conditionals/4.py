fruit = input("Enter the fruit: ")

if fruit=="Banana":
    color = input("Enter the color of the fruit: ")
    if(color=="Green"):
        print("unripe")
    if(color=="Yellow"):
        print("ripe")
    if(color=="Brown"):
        print("Overripe")
else:
    print("We don't have information regarding this fruit.")