# código feito por Chat GPT

import pyautogui as pi
import pyperclip as pcp
import time

def enviar_mensagem(nome, mensagem):
    # Abrir o OperaGX
    pi.hotkey('win')
    pi.write('Opera Gx')
    time.sleep(2)
    pi.click(x=214, y=518)
    time.sleep(8)

    # Clicar no icone do whatsapp
    pi.click(x=18, y=248)
    time.sleep(10)

    # Procurar a pessoa na suas conversas
    pi.click(x=218, y=108)
    pcp.copy(nome)
    pi.hotkey('ctrl', 'v')
    time.sleep(1)
    pi.click(x=202, y=232)

    # Manda a mensagem para essa pessoa
    pcp.copy(mensagem)
    pi.hotkey('ctrl', 'v')
    pi.hotkey('enter')

if __name__ == '__main__':
    # Nome da pessoa e a mensagem
    nome = input('Digite um nome: ')
    mensagem = input('Digite a mensagem desejada:\n')

    enviar_mensagem(nome, mensagem)
