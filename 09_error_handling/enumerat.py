# What is enumerates?
# enumerate is a built-in function that adds a counter to an iterable (like a list or a tuple) 
# and returns it as an enumerate object. This is useful when you need both the index and the 
# value of elements in a loop.

x = ('Masala','Lemon','Ginger')    # tuple
y = enumerate(x)
print(y)                           # <enumerate object at 0x000001A847D30D10>
z=list(y)
print(z)                           # [(0, 'Masala'), (1, 'Lemon'), (2, 'Ginger')]