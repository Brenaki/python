# Challenge - Make a program that checks if a typed letter is "F" or "M". As the letter writes: F - Female, M - Male, Invalid Sex.
import os
def clear():
    return os.system("cls")

# CODE
clear()

# Title
print('==========Decision Structure - Challenges==========')

#Name
name = input('What\'s your name: ')

# Gender
gender = input('What\'s your gender? (M) or (F) or (n-B): ')

# Check
if(gender == 'M' or gender == 'm'):
    print('Your name\'s {} and your gender is masculine'.format(name))
elif(gender == 'F' or gender == 'f'):
    print('Your name\'s {} and your gender is feminine'.format(name))
elif(gender == 'n-B' or gender == 'n-b'):
    print('Your name\'s {} and your gender is non binary'.format(name))
else:
    print('Invalid name and gender')
print('---------------------------------------------------')
