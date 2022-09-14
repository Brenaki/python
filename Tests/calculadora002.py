# Desafio: Fazer uma calculadora mais atualizada!!
import os
import time

def clear():
    return os.system("cls")
clear()

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

def potencia():
    result = num1 ** num2
    return result

def erro():
    return   print('ERROR\n' * 20), print('---------------------------------------------------------------------------')

while True:

    print('--------------------------------CALCULADORA--------------------------------')
    cal = input('Digite o calculo deseja: ')
    if '+' in cal:
        numbers = cal.split('+')
        a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
        if a and b == True:
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            print(adicao())
            write = input('')
            if write in '':
                clear()
        else:
            erro()
            time.sleep(1)
            clear()
            continue
    elif '-' in cal:
        numbers = cal.split('-')
        a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
        if a and b == True:
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            print(subtracao())
            write = input('')
            if write in '':
                clear()
        else:
            erro()
            time.sleep(1)
            clear()
            continue
    elif '*'  in cal or 'x' in cal:
        if '*' in cal:
            numbers = cal.split('*')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(multicacao())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
        elif 'x' in cal:
            numbers = cal.split('x')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(multicacao())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
    elif '/' in cal or ':' in cal:
        if '/' in cal:
            numbers = cal.split('/')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(divisao())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
        elif ':' in cal:
            numbers = cal.split(':')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(divisao())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
    elif '%' in cal:
            numbers = cal.split('%')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(resto_divisao())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
    elif '^' in cal:
            numbers = cal.split('^')
            a, b = numbers[0].isnumeric(), numbers[1].isnumeric()
            if a and b == True:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
                print(potencia())
                write = input('')
                if write in '':
                    clear()
            else:
                erro()
                time.sleep(1)
                clear()
                continue
    elif '' == cal:
        print('---------------------------------------------------------------------------')
        break
    else:
        erro()
        time.sleep(1)
        clear()
        continue
        
