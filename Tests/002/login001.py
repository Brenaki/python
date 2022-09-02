# Fazer uma sistema de login, porém é como se o usuario
# estivesse errando a senha, então pode redefinir a senha
# e poderá logar

while True:
    user = input('Your user: ')
    password = input('Your password: ')
    if password != '':
        if password != '1234' or password != new_P:
            r_pass = input('Quer redifinir sua senha(N/Y): ')
            if r_pass == 'N' or r_pass == 'n':
               continue
            else:
                new_P = input('New password: ')
                password = new_P
                continue
        else:
          break
    else:
      break


