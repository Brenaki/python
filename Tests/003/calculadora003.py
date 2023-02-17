# calculadora feita pelo Chat GPT ultilizando meu código, do calculadora002

import os
import time

def clear():
    os.system("cls")

def adicao(num1, num2):
    return num1 + num2
     
def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def resto_divisao(num1, num2):
    return num1 % num2

def potencia(num1, num2):
    return num1 ** num2

def erro():
    print('ERROR\n' * 20)
    print('---------------------------------------------------------------------------')

while True:
    clear()
    print('--------------------------------CALCULADORA--------------------------------')
    cal = input('Digite o calculo desejado (ou aperte Enter para sair): ')
    
    if not cal:
        break
    
    operacoes = {
        '+': adicao,
        '-': subtracao,
        '*': multiplicacao,
        'x': multiplicacao,
        '/': divisao,
        ':': divisao,
        '%': resto_divisao,
        '^': potencia
    }
    
    operador = None
    for op in operacoes:
        if op in cal:
            operador = op
            break
    
    if not operador:
        erro()
        time.sleep(1)
        continue
    
    numeros = cal.split(operador)
    if not (numeros[0].isnumeric() and numeros[1].isnumeric()):
        erro()
        time.sleep(1)
        continue
    
    num1, num2 = float(numeros[0]), float(numeros[1])
    resultado = operacoes[operador](num1, num2)
    print(resultado)
    input('Pressione Enter para continuar...')
