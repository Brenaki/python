from System import System
import os

def clear():
    return os.system('cls')


def main():
    clear()
    # Sistema de Login e Registro
    print('----------------------------Sistema------------------------------------')
    print('Você deseja se Registrar ou fazer Login?')
    escolha_login_or_register = input('L(login) ou R(registrar): ')

    if escolha_login_or_register.upper() == 'L':
        user = input('Seu nome de usuário: ')
        password = input('Sua senha: ')
        log = System.login(user)
        print(f'{user} entrou no sistema!') if log  == True else print('Credenciais Inválidas!')
    elif escolha_login_or_register.upper() == 'R':
        user = input('Seu nome de usuário: ')
        password = input('Sua senha: ')
        signin = System.sign_in(user, password)
        print(f'{user} foi resgistrado no sistema!') if signin  == True else print(f'{user} já está resgitrado no sistema!')
    else:
        print('Error\n'*20)

if __name__ == '__main__':
    main()