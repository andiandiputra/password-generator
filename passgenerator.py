import random

print('Welcome to the password generator')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_letters = int(input('How many letters would you like for the password ?'))
pass_numbers = int(input('How many numbers would you like for the password ?'))
pass_symbols = int(input('How many symbols would you like for the password ?'))

password = ""

for i in range(0, pass_letters):
    i = random.randint(0,25)
    password += letters[i]
    
for i in range(0, pass_numbers):
    i = random.randint(0,pass_numbers)
    password += numbers[i]

for i in range(0 , pass_symbols):
    i = random.randint(0,8)
    password += symbols[i]

password_list = []

for char in password:
    password_list += char

random.shuffle(password_list)

password_str = ""
for char in password_list:
    password_str += char

print(f"Your new password is : {password_str}")