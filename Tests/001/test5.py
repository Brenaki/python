# Challenge - Make a program that checks if a typed letter is "F" or "M". As the letter writes: F - Female, M - Male, Invalid Sex.

# Title
print('=====Decision Structure - Challenges=====')

#Name
name = input('What\'s your name?\n')

# Gender
gender = input('What\'s your gender? "M" or "F" or "n-B"\n')

# Check
if(gender == 'M'):
    print('Your name\'s {} and your gender is masculine'.format(name))
elif(gender == 'F'):
    print('Your name\'s {} and your gender is feminine'.format(name))
elif(gender == 'n-B'):
    print('Your name\'s {} and your gender is non binary'.format(name))
else:
    print('Invalid name and gender')
