# 5. Default Parameter Value
# </summary>
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"):
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())