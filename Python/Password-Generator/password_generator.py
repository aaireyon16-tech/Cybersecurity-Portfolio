import random
import string

characters = (
    string.ascii_letters
    + string.digits
    + string.punctuation
)

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password) 
