# School of Brazil
import os
def clear():
    return os.system("cls")

# CODE
clear()

print('----------------------School----------------------')
# Name of student
name = input('What\'s your name: ')

# Presence of student
classes = int(input ('How many classes were given: '))
fouls = int(input ('How many fouls: '))
print('--------------------------------------------------')
# Result
result = classes * 0.7
c_att = result - fouls

# Check
if(fouls < result):
    print ('Congratulations!\n{} you attend most classes.\nClasses attendance: {}'.format(name, c_att))
else:
    print('It\'s bad!\n{} you don\'t attend most classes.\nClasses attendance: {}'.format(name, c_att))
print('--------------------------------------------------')

