# Sistema
import os

def clear():
    return os.system("cls")

BD = []

def conectar_bd():
    # Conetando Banco de dados
    import pyodbc

    dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                    'Server=localhost;'
                    'Database=login.db')

    try:
        conexao = pyodbc.connect(dados_conexao)
    except:
        print('Não conectou ao Banco de Dados')
    
    cursor = conexao.cursor()

    # Dividindo as informações
    cursor.execute('SELECT * FROM login')
    valores = cursor.fetchall()
    for colunas in valores:
        ID, username, password = colunas
        BD.append([ID, username, password])
    #Fechando o Banco de Dados
    cursor.close()
    conexao.close()
    return BD

def login(usuario, senha, BD):
    for dados in BD:
        if usuario == dados[1] and senha == dados[2]:
            return print('{} você está logado'.format(usuario))
        else:
            pass
    return print('Credenciais Inválidas!')
    
def registrar(usuario, username, senha, password):
    for dados in BD:
        if usuario != dados[1] and senha != dados[2]:
            # Conetando Banco de dados
            import pyodbc
            dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                        'Server=localhost;'
                        'Database=login.db')
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            # Registrando dados
            cursor.execute('''
        INSERT INTO Login (User, Password)
        VALUES
        ("{}", "{}")
        '''.format(usuario, senha))
            cursor.commit()
            cursor.close()
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