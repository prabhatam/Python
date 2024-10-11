x = 2
y=3
z=4
x+y=?

x+y*z # not a good way instead try to use paranthesis
# (x+y)*z OR x+(y*z)

40 + 2.23 # not a good way to write.
# in above we are combining two type of datatypes, this can lead to fatal error
# for example:- 'ram'+3
# try to write after converting datatype
float(40)+2.23

'chai'+'code' # here + will add both the strings (overloading concept)

x+1, y*2, z/3, z**3 #in a single line we can perform multiple statement operation

2**100 #python can handle such a big number easily

#comparisons
1<2 True
5.0==5.0 True
4.0 != 5.0 True
 
# chained comparison
x<y<z #this statement means x<y and y<z
1==2<3 # this means 1==2 and 2<3

# lets see the math module and it's magic
import math
math.floor(3.5)  # math.floor always gives the lower value of the number
math.floor(-3.5)
math.trunc(2.8)  # math.trunc gives the value closest to the origin
math.trunc(-2,8)

# python can deal with complex numbers also
(1+2j)*3

# lets see the octal numbers, they are represented as 0o78, they always starts with 0o
# another method to convert any number to octal is: oct(num)

# lets see the hexadecimal numbers, they are represented as 0xFF, they always starts with 0X
# another method to convert any number to hexadecimal is: hex(num)

# lets see the binary numbers, they are represented as 0b78, they always starts with 0b
# another method to convert any number to binay is: bin(num)

# bitwise operators (explore more depending upon the application)
x=1
x<<2 = 4 # left shift (multiplies the num by multiples of 2)

import random
random.random() #prints a random value between 0 and 1
random.random(1,100) #prints a random value out of the given range
random.choice([1,2,3,4,5])  # it choses the random value out of the given array
list=[1,2,3,4,5]
random.shuffle(list) # it shuffles the elements of the list randomly


0.1+0.1+0.1-0.3 # this statement does not give result 0
# so, to tackle this type of problem, we use decimal context manager
from decimal import Decimal
Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
# now the above statement gives the correct result that is 0

# similarly we have for fractions also
from fractions import Fraction
myFra = Fraction(2,7)


# now lets discuss about the sets
setone = {1,2,3,4}
setone & {1,3} #output {1,3}
setone | {1,3} #output {1,2,3,4}
setone - {1,2,3,4} #output set()

# lets discuss about the boolean
type(true) #output class 'bool'
True==1 # true
False==0 # true
True+4 # output 5
