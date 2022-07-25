import random

Capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small = "abcdefghijklmnopqrstuvwxyz"
Number = "1234567890"
Symbol = "!@#$%^&*+-=/,.;"

length = 20
string = Capital + Small + Number + Symbol
password = "".join(random.sample(string, length))

print(f"\nYour Password: {password} \n")