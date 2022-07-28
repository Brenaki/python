import pyautogui as pi
import pyperclip as pcp
import time

# 0 - Nome da pessoa e a mensagem
name = input('Digite um nome: ')
msg = input('Digite a mensagem desejada:\n')

# 1 - Abrir o OperaGX
pi.hotkey('win')
pi.write('Opera Gx')
time.sleep(2)
pi.click(x=214, y=518)
time.sleep(8)

# 2 - Clicar no icone do whatsapp
pi.click(x=18, y=248)
time.sleep(10)

# 3 - Procurar a pessoa na suas conversas
pi.click(x=218, y=108)
pcp.copy(name)
pi.hotkey('ctrl', 'v')
time.sleep(1)
pi.click(x=202, y=232)

# 4 - Manda a mensagem para essa pessoa
pcp.copy(msg)
pi.hotkey('ctrl', 'v')
pi.hotkey('enter')