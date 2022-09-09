# Desafio: Fazer uma calculadora!
import os
import time

def clear():
    return os.system("cls")

def adicao():
    result = num1 + num2
    return result
     
def subtracao():
    result = num1 - num2
    return result

def multicacao():
    result = num1 * num2
    return result

def divisao():
    result = num1 / num2
    return result

def resto_divisao():
    result = num1 % num2
    return result

clear()

while True:

    print('--------------------------------CALCULADORA--------------------------------')
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    print('Você deseja:')
    print('1 - somar')
    print('2 - subtrair')
    print('3 - multiplicar')
    print('4 - dividir')
    print('5 - resto da divisão')
    print('---------------------------------------------------------------------------')
    escolhaN = input('')

    while escolhaN == '':
        print('Digite uma as opções, por favor')
        escolha = input('')

    if escolhaN == '1':
        print('O resultado é {}'.format(adicao()))

    elif escolhaN == '2':
        print('O resultado é {}'.format(subtracao()))

    elif escolhaN == '3':
        print('O resultado é {}'.format(multicacao()))

    elif escolhaN == '4':
        print('O resultado é {}'.format(divisao()))

    elif escolhaN == '5':
        print('O resultado é {}'.format(resto_divisao()))

    else:
        print('Não consegui enteder o que você digitou, digite novamente')
        time.sleep(1)
        clear()
        continue

    print('---------------------------------------------------------------------------')
    escolhaE = input('Deseja sair da calculadora? Y/N: ')

    if escolhaE == 'Y' or escolhaE == 'y':
        clear()
        break

    elif escolhaE == 'N' or escolhaE == 'n':
        clear()
        continue
    
    else:
        clear()
        print(20 * '\nError')
        break
