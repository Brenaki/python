# Fazer uma sistema de login, se o usuario
# estivesse errando a senha, ele poderá redefinir a senha
# e assim ele poderá logar

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
            elif r_pass == 'Y' or r_pass == 'y':
                new_P = input('New password: ')
                while new_P != password:
                      user = input('Your user: ')
                      password = input('Your password: ')
                      break
                print('Sua nova senha foi redifinida, com Sucesso!')
                if password == new_P:
                  break
                else:
                  continue
        elif password == '1234' or password == new_P:
            print('Logado!')
            break
    else:
      break
