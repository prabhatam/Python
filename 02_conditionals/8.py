#Problem: Check if a password is "Weak", "Medium", or "Strong". 
# Criteria: <6 chars(weak), 6-10 chars (Medium), >10 chars (strong)

password = input("Enter password: ")
password_length = len(password)

if(password_length<6):
    strength="Weak"
elif(password_length<=10):
    strength = "Medium"
else:
    strength="Strong"

print("Password strength is: ", strength)