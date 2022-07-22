s = input('Write something:\n')

print('The primitive type is ', type(s))

print('Only have spaces?\n{}'.format(s.isspace()))

print('It\'s a number?\n{}'.format(s.isnumeric()))

print('It\'s alphabetical?\n{}'.format(s.isalpha()))

print('It\'s alphanumeric?\n{}'.format(s.isalnum()))

print('Is it capital?\n{}'.format(s.isupper()))

print('Is it lowercase?\n{}'.format(s.islower()))

print('Is it capitalized?\n{}'.format(s.istitle()))
