# run these in the terminal and see the output

tea_varities = ["Black","Green","Oolong","White"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[1])
print(tea_varities[-1])
print(tea_varities[1:3])
print(tea_varities[:2])
print(tea_varities[2:])
tea_varities[3]="Herbal"
print(tea_varities)

tea_varities = ["Black","Green","Oolong","White"]
tea_varities[1:2] = ["Lemon"] #green is replaced by lemon
print(tea_varities)
tea_varities[1:3]=["green","Masala"]
print(tea_varities)

tea_varities = ["Black","Green","Oolong","White"]
print(tea_varities[1:1]) #output is []
tea_varities[1:1]=["test","test"]
print(tea_varities)
tea_varities[1:3]=[]
print(tea_varities)

tea_varities = ["Black","Green","Masala","White"]
for tea in tea_varities:
    print(tea)
for tea in tea_varities:
    print(tea, end="-") #output will be in one line having - in between the elements
if "Oolong" in tea_varities:
    print("I have Oolong tea")
tea_varities.append("Oolong")
print(tea_varities)
if "Oolong" in tea_varities:
    print("I have Oolong tea")


tea_varities = ["Black","Green","Masala","White","Oolong"]
tea_varities.pop() #removes the last element
print(tea_varities)
tea_varities.remove("Green")
print(tea_varities)

tea_varities.insert(1,"green")
print(tea_varities)

tea_varities_copy=tea_varities.copy() 
# by doing this both variables will not have same reference
# they will be pointing to other other objects
tea_varities_copy.append("Lemon")
print(tea_varities_copy)
print(tea_varities)

range(10)
print(range(10))
squared_num = [x**2 for x in range(10)]
print(squared_num)
cube_num = [y**3 for y in range(5)]
print(cube_num)







# In Python, a list is one of the most commonly used data structures. 
# It is a mutable, ordered collection that can store elements of any data type. 
# Here's a theoretical breakdown and an explanation of how lists work behind the scenes:

# Theoretical Overview:
# Definition: A list is a dynamic array that can hold items of various data types 
# (integers, floats, strings, other lists, etc.). Lists are ordered, 
# meaning that the elements are indexed, starting from 0.

# Syntax:

# python
# Copy code
# my_list = [1, 2, 3, 4]
# Mutable: Lists in Python are mutable, meaning that once a list is created, 
# you can change, add, or remove elements.

# Example of mutability:

# python
# Copy code
# my_list[1] = 5  # Changes the second element from 2 to 5
# Indexing and Slicing: Lists support indexing (accessing elements by their index) 
# and slicing (extracting a sublist). Indexes in Python are 0-based 
# (i.e., the first element is at index 0).

# Example:

# python
# Copy code
# my_list = [10, 20, 30, 40]
# print(my_list[0])  # Outputs 10 (first element)
# print(my_list[-1])  # Outputs 40 (last element)
# Slicing:

# python
# Copy code
# print(my_list[1:3])  # Outputs [20, 30] (second and third elements)
# Dynamic Size: Lists in Python can grow and shrink dynamically. 
# This means that you don't have to specify a fixed size during list creation.

# Example:

# python
# Copy code
# my_list.append(50)  # Adds 50 to the end of the list
# Heterogeneous Data: Lists can hold elements of different data types.

# python
# Copy code
# my_list = [1, "hello", 3.14, True]  # Integer, String, Float, Boolean
# Common Methods: Python provides a rich set of list operations 
# such as adding, removing, or manipulating elements.

# append(): Adds an item to the end of the list.
# extend(): Adds multiple items to the end.
# insert(): Inserts an item at a specific index.
# remove(): Removes the first occurrence of a value.
# pop(): Removes an item by index (default is the last element).
# sort(): Sorts the list in place.
# reverse(): Reverses the list in place.

# Behind the Scenes:
# Dynamic Array Implementation: Behind the scenes, Python lists are implemented as dynamic arrays. 
# This means the underlying structure of a list is an array, but with the ability to resize when needed.

# Initial Memory Allocation: When you create a list, Python allocates a block of memory to store the elements. It also allocates extra space to handle future insertions without needing to resize the list every time you add an element.

# Automatic Resizing: When the list exceeds its allocated space, 
# Python resizes it by allocating a new, larger block of memory and copying the old elements into it. 
# Typically, the size is increased by a factor (e.g., 1.5x or 2x the current capacity).

# This resizing ensures that list appends are amortized O(1) in terms of time complexity, 
# meaning that while individual append operations may occasionally take more time (during a resize), 
# the average time per append operation is constant.

# Memory Management:

# Lists in Python are just references to objects. When you store an element in a list, 
# Python doesn't store the actual value in the list; instead, it stores a reference (or pointer) 
# to the actual object in memory.
# This is why lists can contain different data types: Python simply stores references to 
# objects in the list, and these objects can be of any type.


# Time Complexity of Operations:

# Accessing an element (indexing) is O(1) because lists use an array-like structure 
# where elements can be accessed by their index directly.
# Appending an element is amortized O(1), as mentioned earlier, due to dynamic resizing.
# Inserting an element at the start or in the middle has a time complexity of O(n) because 
# elements may need to be shifted.
# Removing an element (e.g., using pop()) from the end is O(1), but removing from the middle is O(n), 
# as elements must be shifted to fill the gap.


# Shallow Copy vs. Deep Copy:

# A shallow copy of a list (created using list.copy() or list[:]) creates a new list, 
# but the elements in both lists still refer to the same objects.
# A deep copy (created using the copy module’s deepcopy() method) creates a new list with all new elements, 
# recursively copying all objects in the list.

# Summary of List Internals:
# Lists are backed by dynamic arrays, with extra space pre-allocated to reduce the frequency of resizing.
# Lists are mutable and can grow or shrink dynamically.
# Python lists store references to objects rather than the actual objects.
# Operations such as accessing, appending, and removing elements have varying time complexities 
# depending on the operation and position.
