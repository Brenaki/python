# Sistema
import os
from random import randrange
import mysql.connector

def clear():
    return os.system("cls")

BD = []

def conectar_bd():
    # Conetando Banco de dados
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
    )

    mycursor = mydb.cursor()

    # Dividindo as informações
    mycursor.execute("USE login")
    mycursor.execute("SELECT * FROM Login")
    valores = mycursor.fetchall()
    for colunas in valores:
        ID, username, password = colunas
        BD.append([ID, username, password])
    #Fechando o Banco de Dados
    mycursor.close()
    mydb.close()
    return BD

def login(usuario, senha, BD):
    for dados in BD:
        if usuario == dados[1] and senha == dados[2]:
            return print('{} você está logado'.format(usuario))
        else:
            pass
    return print('Credenciais Inválidas!')
    
def registrar(usuario, senha, BD):
    # Gerar ID
    ID = randrange(2, 1000)
    # Conetando Banco de dados
    for dados in BD:
        if usuario != dados[1] and senha != dados[2]:
            # Conetando Banco de dados
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="login"
            )
            mycursor = mydb.cursor()
            # Registrando dados
            mycursor.execute("INSERT INTO `login`.`Login` (`ID`, `User`, `Password`) VALUES ('{}','{}', '{}');".format(ID, usuario, senha))
            mydb.commit()
            mycursor.close()
            mydb.close()
            return print('{} você foi registrado!'.format(usuario))
        else:
            pass
    return print('Usuário já está resgitrado!')

clear()

# Conetando BD
conectar_bd()
    
# Sistema de Login e Registro
print('----------------------------Sistema------------------------------------')
print('Você deseja se registrar ou fazer login?')
escolha_login_or_register = input('L(login) ou R(registrar): ')

if escolha_login_or_register == 'L' or escolha_login_or_register == 'l':
    usuario = input('Seu nome de usuário: ')
    senha = input('Sua senha: ')
    login(usuario, senha, BD)
elif escolha_login_or_register == 'R' or escolha_login_or_register == 'r':
    usuario = input('Seu nome de usuário: ')
    senha = input('Sua senha: ')
    registrar(usuario, senha, BD)
else:
    print('Error\n'*20)