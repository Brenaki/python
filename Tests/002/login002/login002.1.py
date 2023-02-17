# Código feito pelo chat GPT

import os
import random
import mysql.connector

# Define o nome do banco de dados
DATABASE_NAME = 'login'

def clear():
    """
    Limpa a tela do terminal.
    """
    os.system('cls')

def connect_database():
    """
    Conecta ao banco de dados e retorna a conexão.
    """
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database=DATABASE_NAME
    )

    return connection

def disconnect_database(connection):
    """
    Encerra a conexão com o banco de dados.
    """
    connection.close()

def fetch_users(connection):
    """
    Busca os usuários no banco de dados e retorna uma lista com os dados.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Login')
    rows = cursor.fetchall()
    cursor.close()

    users = []
    for row in rows:
        users.append({'id': row[0], 'username': row[1], 'password': row[2]})

    return users

def login(username, password, users):
    """
    Faz o login do usuário no sistema.
    """
    for user in users:
        if username == user['username'] and password == user['password']:
            print('{} você está logado'.format(username))
            return

    print('Credenciais Inválidas!')

def register(username, password, connection, users):
    """
    Registra um novo usuário no sistema.
    """
    # Verifica se o usuário já está cadastrado
    for user in users:
        if username == user['username']:
            print('Usuário já está registrado!')
            return

    # Gera um novo ID
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(ID) FROM Login')
    max_id = cursor.fetchone()[0] or 1
    new_id = random.randint(max_id + 1, 1000)

    # Insere o novo usuário no banco de dados
    cursor.execute('INSERT INTO Login (ID, User, Password) VALUES (%s, %s, %s)', (new_id, username, password))
    connection.commit()
    cursor.close()

    print('{} você foi registrado!'.format(username))

def main():
    """
    Função principal do programa.
    """
    clear()

    # Conecta ao banco de dados
    connection = connect_database()

    # Busca os usuários no banco de dados
    users = fetch_users(connection)

    # Pergunta se o usuário quer fazer login ou registro
    print('----------------------------Sistema------------------------------------')
    print('Você deseja se registrar ou fazer login?')
    choice = input('L (login) ou R (registrar): ')

    # Faz o login ou o registro
    if choice.lower() == 'l':
        username = input('Seu nome de usuário: ')
        password = input('Sua senha: ')
        login(username, password, users)
    elif choice.lower() == 'r':
        username = input('Seu nome de usuário: ')
        password = input('Sua senha: ')
        register(username, password, connection, users)
    else:
        print('Opção inválida!')

    # Encerra a conexão com o banco de dados
    disconnect_database(connection)

if __name__ == '__main__':
    main()
