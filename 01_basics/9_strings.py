chai = "lemon chai"
print(chai)

new_chai = "masala chai"
first_char = new_chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai) #output is masala

print(chai[-1]) #output is i

numlist="0123456789"
print(numlist[:]) #output is 0123456789
print(numlist[3:])#output is 3456789
print(numlist[:7])#output is 0123456
print(numlist[0:7:2]) #output is 0246
print(numlist[0:7:3]) #output is 036

chai_one = "Ginger tea"
print(chai_one.upper())
print(chai_one.lower())


chai = "  masala chai   "
print(chai.strip()) #it removes all the spaces from before and after the string

chai = "lemon chai"
print(chai.replace("lemon","ginger")) #ginger chai

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", ")) #it splits and converts into list based on the given condition

chai = "Masala Chai"
print(chai.find("Chai")) #output is 7 that means chai starts from 7th position
print(chai.find("chai")) # output is -1 that means it does not find such string

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")) # 3

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type)) #output:- I ordered 2 cups of Masala chai

#lets convert from list to string
chai_variety = ["Lemon", "Masala","Ginger"]
print(",".join(chai_variety)) #output is: Lemon,Masala,Ginger
print(" ".join(chai_variety)) #output is: Lemon Masala Ginger
print(", ".join(chai_variety)) #output is: Lemon, Masala, Ginger

chai = "Masala chai"
print(len(chai)) #11

#print one one letter of chai
for letter in chai:
    print(letter)



#initially due to first two double quote it would have end but by using \ solved the problem
chai = "He said, \"Masala chai is awesome\" "

chai = "Masala\nChai"
print(chai) #output is Masala and Chai in two lines
chai = r"Masala\Chai"  # this prints the raw string
print(chai) #output is Masala\Chai

path = r"c:\\user\\pwd\\"
print(chai) #output: c:\\user\\pwd\\

path1=r"c:\user\pwd"
print(path1)   # output: c:\user\pwd
# \ in the last creates the problems



chai = "Masala Chai"
print("Masala" in chai) #output True










# chatgpt

'''
In Python, strings are a core data type used to represent sequences of characters. They are one of the most commonly used types in programming for text manipulation. Let's dive into the theoretical concepts and behind-the-scenes implementation of strings.

Theoretical Overview:
Definition: A string in Python is an immutable sequence of Unicode characters, which means once a string is created, it cannot be modified.

Syntax:

python
Copy code
my_string = "Hello, World!"
Immutable: Strings in Python are immutable, meaning that once a string object is created, it cannot be changed. Any operation that seems to modify a string actually creates a new string object.

Example:

python
Copy code
s = "Hello"
s[0] = 'h'  # This will raise a TypeError because strings are immutable.
Instead, to "modify" a string, you must create a new one:

python
Copy code
s = "Hello"
new_s = 'h' + s[1:]  # Outputs 'hello'
Unicode Support: Python strings are represented as sequences of Unicode characters, meaning they can support a vast range of characters from different languages and symbol sets.

Indexing and Slicing: Like lists, strings are indexed and support slicing. They are 0-indexed, meaning the first character is at index 0.

Example:

python
Copy code
s = "Python"
print(s[0])   # Outputs 'P'
print(s[-1])  # Outputs 'n'
Slicing:

python
Copy code
print(s[1:4])  # Outputs 'yth'
Concatenation and Repetition: Strings support basic operations like concatenation (using the + operator) and repetition (using the * operator).

Example:

python
Copy code
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # Outputs "Hello World"
Repetition:

python
Copy code
repeated = "Hi" * 3  # Outputs "HiHiHi"
Common Methods: Strings in Python come with a variety of built-in methods to manipulate text. Some important ones are:

lower(): Converts the string to lowercase.
upper(): Converts the string to uppercase.
split(): Splits the string into a list based on a delimiter.
join(): Joins elements of a list into a string with a separator.
replace(): Replaces occurrences of a substring with another.
strip(): Removes leading and trailing whitespace.
find(): Returns the index of the first occurrence of a substring.
format(): Formats the string using placeholders.
Example:

python
Copy code
s = " Hello, World! "
print(s.strip())  # Outputs "Hello, World!"
Behind the Scenes:
Storage: Python strings are stored as a sequence of Unicode characters in memory. Each character in a string is represented by a code point (a unique number). Python internally stores strings as UTF-8 or UTF-16 depending on the environment.

Immutability and Memory Management:

Immutability means that once a string is created, its memory cannot be changed. If you perform any operation on a string that appears to modify it, Python will actually create a new string object in memory, leaving the original string unchanged.
This immutability makes strings memory efficient in certain scenarios. Since strings are immutable, Python can internally reuse them when necessary (this process is called string interning).
Example of interning:

python
Copy code
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True, both point to the same string object
String Interning: Python optimizes memory usage through a mechanism called string interning, which involves reusing memory for identical strings, especially shorter strings or those that look like identifiers (e.g., variable names).

Python will reuse the memory of a string instead of creating a new one for certain types of strings, like literals and small strings.
This process happens automatically, but developers can force interning using sys.intern().
Example:

python
Copy code
a = "hello"
b = "hello"
print(a is b)  # Outputs True because both refer to the same interned string.
Memory Efficiency: Since strings are immutable, Python can optimize memory allocation for them. For instance, slicing a string does not create a new string immediately but references the same memory until the sliced string is modified.

Example:

python
Copy code
s = "Python is awesome"
s_slice = s[0:6]  # Slicing the first word
Time Complexity of Operations:

Indexing (accessing a specific character) is O(1) because strings are stored as arrays of characters.
Concatenation is O(n), where n is the total length of the new string. This is because strings are immutable, and concatenation creates a new string with the contents of both original strings.
Slicing creates a new string, which is also O(n), where n is the length of the slice.
Searching (find, index, etc.) is O(n) because Python may have to scan the entire string to find a match.
Encoding: Python strings are Unicode by default, but they can be encoded to various formats (like UTF-8, ASCII) using the encode() method. Conversely, encoded data can be decoded back into a string using the decode() method.

Example:

python
Copy code
s = "Hello"
encoded_s = s.encode('utf-8')  # Encodes the string to UTF-8
decoded_s = encoded_s.decode('utf-8')  # Decodes it back to a string
Important Points about Python Strings:
Immutable:

Strings cannot be changed in place. Operations that appear to modify strings create new strings.
Unicode Support:

Python strings are sequences of Unicode characters, allowing them to represent text from any language, special symbols, and emojis.
String Pooling and Interning:

Python automatically manages memory efficiently for strings through interning, especially for frequently used strings (like literals).
Efficient Memory Use:

Slicing strings doesn’t immediately copy the data, and Python tries to minimize memory usage through reference counting and other techniques.
Time Complexity:

Most string operations (like indexing and accessing) are efficient (O(1)), but operations like concatenation and searching can have a higher complexity, depending on the length of the string.
String Methods:

Strings come with many powerful built-in methods for manipulation (e.g., split(), join(), replace(), upper(), lower()), making them highly versatile for text processing tasks.
Summary of String Internals:
Strings are immutable, meaning any modification results in a new string object being created.
Python stores strings as sequences of Unicode characters.
Memory optimization techniques like string interning help save space and increase efficiency.
String operations have different time complexities based on the operation (e.g., concatenation is O(n), indexing is O(1)).
'''