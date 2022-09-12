# Fazer uma sistema de login, se o usuario
# estivesse errando a senha, ele poderá redefinir a senha
# e assim ele poderá logar
import os
import time

def clear():
    return os.system("cls")

clear()

newP = '1234'

while True:
    user = input('Seu username: ')
    password = input('Sua senha: ')
    if password != '': 
        if password != newP and not '1234' in password :
            print('Senha inválida')
            r_pass = input('Quer redifinir sua senha(S/N): ')
            if r_pass == 'N' or r_pass == 'n':
               continue
               time.sleep(1)
               clear()
            elif r_pass == 's' or r_pass == 's':
                clear()
                new_P = input('Nova senha: ')
                print('Sua nova senha foi redifinida, com Sucesso!')
                time.sleep(0.5)
                clear()
                while newP != password:
                      user = input('Seu username:  ')
                      password = input('Sua senha: ')
                      break
                print('{} foi logado!'.format(user))
                break
                if password == newP:
                  break
                else:
                  continue
        elif password == '1234' or password == newP:
            print('{} foi logado!'.format(user))
            break
    else:
      break
