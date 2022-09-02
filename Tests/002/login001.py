# Fazer uma sistema de login, porém é como se o usuario
# estivesse errando a senha, então pode redefinir a senha
# e poderá logar

user = input('Your user: ')
password = input('Your password: ')

while True:
    user = input('Your user: ')
    password = input('Your password: ')
    if password != '':
        while password != '1234':
            r_pass = input('Quer redifinir sua senha(N/Y): ')
            if r_pass == 'N' or r_pass == 'n':
               password = input('Your password: ')
            else:
                new_password = input('New password: ')
                password = new_password


