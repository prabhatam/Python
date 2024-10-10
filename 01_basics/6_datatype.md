# Object Types/ Data Types  # (using # we make comments) 

- number: 1234, 3.1415, 3+4j, 0b11, Decimal(), Fraction()

- String: 'spam', "bob's",b'a\x01c, u'sp\xc4m

# [] - square brackets, () - parenthesis, {}-braces

- List: [1, [2,'three'], 4.5], list(range(10))

- Tuple: (1,'spam',4,'U'), tuple('spam'), namedtuple

- Dictionary: {'food': 'spam','taste':'yum'}, dict(hours=10)

- Set: set('abc'), {'a','b','c'}

- File: open('eggs.txt'),open(r'C:\ham.bin','wb')

-Boolean : True, False

-None: None

-Functions, modules, classes

- Advance: Decorators, Generators, Iterators, Metaprogramming

examples:

2**100=?

import math
math.pi # gives the value of pi

import random
random.random() # prints a random value

random.choice([1,2,3,4]) # it choses value randomly

username = "chaiaurcode"
len(username) #prints the length of the username
username[0] # prints the specific elements of the string 
username[0]='p' # it gives error because string is immutable
username[-1]  #prints the first element from last
username[-2]  #prints the second element from last

# it is same as  array and starts with square brackets []
mylist = [123, "chai", 3.14]
print(mylist)
len(mylist)
mylist(0)
mylist(-1)

# dictionary starts with curly braces {}
# it exists in key:value pairs
myD = {'one':'lemon','two':'ginger','three':'naagraj'}
print(myD)
myD['two'] # prints the corresponding value to key given

# tuples starts with braces paranthesis
myTup = (1,2,3,4)
print(myTup[0])
len(myTup)

