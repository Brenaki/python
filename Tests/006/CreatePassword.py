import random
import os

# Clear a prompt
def clear():
    return os.system("cls")
clear()

def portuguese():
    try:
# Def para os ifs
        def sem_letras(qtd_caracteres):
            caracter = '123456789!@#$%^&*()'
            for sen in range(0,1):
                senha = ''
                for c in range(qtd_caracteres):
                    senha += random.choice(caracter)
            return senha
        def sem_numeros(qtd_caracteres):
            caracter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST!@#$%^&*()'
            for sen in range(0,1):
                senha = ''
                for c in range(qtd_caracteres):
                    senha += random.choice(caracter)
            return senha
        def sem_simbolos(qtd_caracteres):
            caracter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST1234567890'
            for sen in range(0,1):
                senha = ''
                for c in range(qtd_caracteres):
                    senha += random.choice(caracter)
            return senha
        def senha(qtd_caracteres):
            caracter = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRST!@#$%^&*()'
            for sen in range(0,1):
                senha = ''
                for c in range(qtd_caracteres):
                    senha += random.choice(caracter)
            return senha

# Sim ou Não
        print('S = Sim e N = Não')

# Escolha as configurações
        letras = input('Com letras: ')
        numeros = input('Com números: ')
        simbolos = input('Com símbolos: ')
        qtd_caracteres = int(input('Quantos dígitos: '))
# Estrutura de Decisão
## Senha aleatória
        if letras.upper() == 'S' and numeros.upper() == 'S' and simbolos.upper() == 'S':
            print(f'\nAqui a sua senha:\n{senha(qtd_caracteres)}')
## Sem Letras
        elif letras.upper() != 'S' and numeros.upper() == 'S' and simbolos.upper() == 'S':
            print(f'\nAqui a sua senha:\n{sem_letras(qtd_caracteres)}')
## Sem números
        elif letras.upper() == 'S' and numeros.upper() != 'S' and simbolos.upper() == 'S':
            print(f'\nAqui a sua senha:\n{sem_numeros(qtd_caracteres)}')
## Sem símbolos
        elif letras.upper() == 'S' and numeros.upper() == 'S' and simbolos.upper() != 'S':
            print(f'\nAqui a sua senha:\n{sem_simbolos(qtd_caracteres)}')
    except:
        print('Digite um número inteiro!')
def english():
    try:
# Def for if
        def not_letters(lenght):
            char = '123456789!@#$%^&*()'
            for pwd in range(0,1):
                passwords = ''
                for c in range(lenght):
                    passwords += random.choice(char)
            return passwords
        def not_numbers(lenght):
            char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST!@#$%^&*()'
            for pwd in range(0,1):
                passwords = ''
                for c in range(lenght):
                    passwords += random.choice(char)
            return passwords
        def not_symbols(lenght):
            char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST1234567890'
            for pwd in range(0,1):
                passwords = ''
                for c in range(lenght):
                    passwords += random.choice(char)
            return passwords
        def password(lenght):
            char = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRST!@#$%^&*()'
            for pwd in range(0,1):
                passwords = ''
                for c in range(lenght):
                    passwords += random.choice(char)
            return passwords

# Yes or No
        print('Y = Yes and N = No')

# Choose the settings
        letters = input('How letters: ')
        numbers = input('How Number: ')
        symbols = input('How Symbols: ')
        how_many_digits = int(input('How many digits: '))
# Structure Decision
## All caracter
        if letters.upper() == 'Y' and numbers.upper() == 'Y' and symbols.upper() == 'Y':
            print(f'\nHere is your password:\n{password(how_many_digits)}')
## Not letters
        elif letters.upper() != 'Y' and numbers.upper() == 'Y' and symbols.upper() == 'Y':
            print(f'\nHere is your password:\n{not_letters(how_many_digits)}')
## Not numbers
        elif letters.upper() == 'Y' and numbers.upper() != 'Y' and symbols.upper() == 'Y':
            print(f'\nHere is your password:\n{not_numbers(how_many_digits)}')
## Not symbols
        elif letters.upper() == 'Y' and numbers.upper() == 'Y' and symbols.upper() != 'Y':
            print(f'\nHere is your password:\n{not_symbols(how_many_digits)}')
    except:
        print('Please enter a number interger!')

# Choose a idiom // Escolha o idioma
print('What is your language? E - English or P - Portuguese // Qual seu idioma? I - Inglês ou P - Português')
language = input('')

# Structure Decision // Estructura de Decisão
if language.upper() == 'E' or language.upper() == 'I':
    english()
elif language.upper() == 'P':
    portuguese()
else:
    print('Invalid language! // Idioma inválido!')