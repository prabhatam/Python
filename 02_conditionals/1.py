# to take user input we use "input"
# input taken can be anything 
# we need to make sure that we change the datatype of the incoming data as per our requirement

age=int(input("Provide me an age:"))
if age<13:
    print("Child")
elif(age<20):
    print("Teenager")
elif(age<59):
    print("Adult")
else:
    print("Senior")