import random
import time

capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

password = ""

print("Hello o/")
capital_numbers = int(input("How many Capital Letters you want? "))
small_numbers = int(input("How many Small Letters you want? "))
numbers_numbers = int(input("How many Numbers you want? "))
symbols_numbers = int(input("How many Symbols you want? "))

for i in range(0, capital_numbers):
    password += capital[random.randint(0, 25)]
for i in range(0, small_numbers):
    password += small[random.randint(0, 25)]
for i in range(0, numbers_numbers):
    password += numbers[random.randint(0, 9)]
for i in range(0, symbols_numbers):
    password += symbols[random.randint(0, 9)]

password_list = list(password)
random.shuffle(password_list)
new_password = ""
for pw in password_list:
    new_password += pw

print("\n Password Generated! \n")
time.sleep(0.5)
print(f"\n Your Password: {new_password} \n")