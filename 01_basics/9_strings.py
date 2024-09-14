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
print(chai.find("Chai"))
print(chai.find("chai"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type)) #output:- I ordered 2 cups of Masala chai

#lets convert from list to string
chai_variety = ["Lemon", "Masala","Ginger"]
print(",".join(chai_variety)) #output is: Lemon,Masala,Ginger

chai = "Masala chai"
print(len(chai))

#print one one letter of chai
for letter in chai:
    print(letter)



#initially due to first two double quote it would have end but by using \ solved the problem
chai = "He said, \"Masala chai is awesome\" "

chai = "Masala\nChai"
print(chai) #output is Masala Chai
chai = r"Masala\Chai"
print(chai) #output is Masala\Chai

path = r"c:\\user\\pwd\\"
print(chai)

path1=r"c:\user\pwd"
print(path1)
# \ in the last creates the problems



chai = "Masala Chai"
print("Masala" in chai) #output True

