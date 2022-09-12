# School of Brazil

import os
def clear():
    return os.system("cls")

# CODE
clear()
print('--------------------__School__--------------------\n')

# Name
name = input ('What\'s your name?\n')

# Grades
n1 = int(input ('Write fist number:\n'))
n2 = int(input ('Write second number:\n'))
n3 = int(input ('Write third number:\n'))
n4 = int(input ('Write fourth number:\n'))

# Result
average = (n1+n2+n3+n4)/4

# Check
if(average >= 6):
    print('{}, you passed the year. Your average was {}!'.format(name, average))
else:
    print('{}, you don\'t passed the year. Your average was {}!'.format(name, average))      