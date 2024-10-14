# why do we need tuples?
# list is mutable -> changes in the memory
# we needed similar type of data structure which is immutable so tuples came into existence
# tuples is immutuable
# we use () for tuples
# tuples are almost same as list
# tupeles and list both have 0 based indexing
tea_types = ("black","green","oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])
# tea_types[0] = "lemon" #this give error because tuples are immutable
print(len(tea_types))

more_tea = ("Herbal","Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "green" in all_tea:
    print("I have green tea.")

more_tea = ("Herbal", "Earl Grey","Herbal")
print(more_tea)
print(more_tea.count("Herbal"))

# suppose some output is coming from the db which contains tea_types
# and we want to get them into variables 
# then by taking no. of variables = no. of items in the tea_types, it is possible
tea_types = ("Black","Green","Oolong")
(black,green,oolong) = tea_types
print(black) # output is Black

# lets say we want to the type of a varialbe then 
print(type(tea_types)) # <class 'tuple'>

# nesting of tuples
("",(1,2,3),"")