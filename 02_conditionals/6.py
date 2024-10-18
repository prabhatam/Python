# Problem: Choose a mode of transportation based on 
# the distance (e.g., <3km: walk, 3-15km: bike, > 15 km:car)

distance = int(input("Enter the distance to decide the mode of transportation: "))

if(distance<3):
    print("Walk")
elif(distance<=15):
    print("Bike")
else:
    print("car")