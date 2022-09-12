# Challenge - Make a program that asks for two numbers and prints the largest of them!
import os
def clear():
    return os.system("cls")

# CODE
clear()

# Title
print('=============Decision Structure - Challenges=============')

# Numbers
n1 = int(input ('Write fist number: '))
n2 = int(input ('Write second number: '))

# Check
if(n1 > n2):
    print('The first number is greater than the second number. {} > {}'.format(n1, n2))
else:
    print('The second number is greater than the fist number. {} > {}'.format(n2, n1))
print('---------------------------------------------------------')
