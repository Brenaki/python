# Escola do Brazil
import os
def clear():
    return os.system("cls")

# CODE
clear()
print('----------------------Escola----------------------')

# Name
name = input ('Qual o nome do aluno: ')

# Grades
qtde_B = int(input('Quantos tri/bimestres teve esse ano: '))
ano = []

print('--------------------------------------------------')
for i in range(qtde_B):
    number = float(input('Nota do {}º Tri/Bimestre:  '.format(i+1)))
    bit = [number]
    ano.append(bit)
print('--------------------------------------------------')

media = 0

for a in ano:
    if media == a[0]:
        media += media
    else:
        media += a[0]

# Result
mediaF = media / qtde_B

# Check
if(mediaF >= 6):
    print('{}, você passou de ano!\nSua média foi de {:.2}.'.format(name, mediaF))
elif (mediaF >= 4):
    print('{}, você foi para recuperação!\nSua média foi de {:.2}.'.format(name, mediaF))
else:
    print('{}, você não passou de ano! :c\nSua média foi de {:.2}.'.format(name, mediaF))
print('--------------------------------------------------')
