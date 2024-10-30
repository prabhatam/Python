# how to open a file if it exists
# file = open('09_error_handling/test.py')


# we can give mode to the files at the time of opening it

# lets see the write mode
file1 = open('09_error_handling/xyz.py','w') 
file1.close()
# this above line opens the file in write mode if it exits
# otherwise it creates the file
# we need to use it very cautiously


# after opening the file and after performing read or write operation, we need to close the file too.
file2 = open('09_error_handling/youtube.txt', 'w')
try:
    file2.write('chai aur code')
finally:
    file2.close()

# alternative way to do the above task is below
with open('09_error_handling/z.txt', 'w') as file3:
    file3.write('chai aur python')