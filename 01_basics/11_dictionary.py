#run these commands in the terminal and get the output

chai_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# dictionaries are in the key value pair forms.
print(chai_types)
print(chai_types["Masala"]) #output- Spicy # how to access values using keys.
chai_types.get("Ginger") #output- Zesty
chai_types.get("Gingery") #returns nothing

# we can change the items of the dictionary
chai_types["Green"] = "Fresh"
print(chai_types)

# lets look into iterations/loop
for chai in chai_types:
    print(chai)
# output - it returns only keys of the dictionary
# Masala
# Ginger
# Green

# how we can print values too
for chai in chai_types:
    print(chai, chai_types[chai])
# Masala Spicy
# Ginger Zesty
# Green Fresh

# we can print key and value at same time also
for key, value in chai_types.items():
    print(key,value)
# Masala Spicy
# Ginger Zesty
# Green Fresh

# we can aslo ask questions that whether this key is present or not in the dictionary
if "Masala" in chai_types:
    print("I have masala chai")
# output I have masala chai

# how to find the length of the dictionary
print(len(chai_types)) # output: 3 bcz there are three elements in the dictionary
print(chai_types)

# how to add a new item to the dictionary
chai_types["Earl Grey"] = "Citrus" # this will add this new item to the chai_types
print(chai_types)

# how to delete an item
chai_types.pop("Ginger") # it will delete the key and value of Ginger item
# we need to mention the key in case of pop to delete an item
# but if we want to delete the last item from the chai_types then
chai_types.popitem() # this will delete the last item from the chai_types
print(chai_types)
del chai_types["Masala"] #by using this also we can delete the item

# lets see how we can make a new copy
chai_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
chai_types_copy = chai_types.copy() # remember about the objects refence concept
print(chai_types_copy)

# lets see the concept of dictionary inside dictionary
tea_shop = {
    "chai":{"masala":"spicy","ginger":"zesty"},
    "tea" :{"green":"mild","black":"strong"}
    }
print(tea_shop) # it will print all the items as per dictionary rules
print(tea_shop["chai"])
print(tea_shop["chai"]["ginger"]) #output zesty

# lets see the squared concept with the help of dictionary
squared_num = {x:x**2 for x in range(6)}
print(squared_num)
squared_num.clear() # this will clear the squared_num dictionary
print(squared_num)

# lets create dictionary from list(array) and assign values  to the keys
keys = ["masala", "ginger", "lemon"]
default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)