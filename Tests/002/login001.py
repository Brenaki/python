# Fazer uma sistema de login, porém é como se o usuario
# estivesse errando a senha, então pode redefinir a senha
# e poderá logar
from ast import Break


new_P = '1234'

while True:
    user = input('Your user: ')
    password = input('Your password: ')
    if password != '': 
        if password != new_P and not '1234' in password :
            print('Senha inválida')
            r_pass = input('Quer redifinir sua senha(N/Y): ')
            if r_pass == 'N' or r_pass == 'n':
               continue
            else:
                new_P = input('New password: ')
                while password != new_P:
                      user = input('Your user: ')
                      password = input('Your password: ')
                print('Sua nova senha foi redifinida!')
                continue
        elif password == '1234' or password == new_P:
            print('Logado!')
            break
    else:
      break


