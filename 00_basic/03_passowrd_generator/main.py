# A project on Understanding Loops in python
import random

print("Welcome to Password Generator!")

password = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
syms = ['#', '@', '!', '$', '%', '^', '&', '*', '(', ')']

l = int(input("How many letters would you like in your password ?\n"))
for i in range(0, l):
    password.append(random.choice(letters))

s = int(input("How many symbols would you like in your password ?\n"))
for i in range(0, s):
    password.append(random.choice(syms))

n = int(input("How many numbers would you like in your password ?\n"))
for i in range(0, n):
    password.append(str(random.randint(0, 9)))

random.shuffle(password)

for i in password:
    print(i, end="")
print()
