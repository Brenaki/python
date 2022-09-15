from cgitb import text
from tkinter import *

def one():
    text = 1
    return text

janela = Tk()
janela.title("Calculadora")
texto = Label(janela, text="")
texto.grid(column=0, row=0, padx=10, pady=10)

um = Button(janela, text="1", command=one())
tres = Button(janela, text="3")
dois = Button(janela, text="2")
quatro = Button(janela, text="4")
cinco = Button(janela, text="5")
seis = Button(janela, text="6")
sete = Button(janela, text="7")
oito = Button(janela, text="8")
nove = Button(janela, text="9")
zero = Button(janela, text="0")

sete.grid(column=1, row=1, padx=5, pady=5)
oito.grid(column=2, row=1, padx=5, pady=5)
nove.grid(column=3, row=1, padx=5, pady=5)
zero.grid(column=2, row=4, padx=5, pady=5)
um.grid(column=1, row=3, padx=5, pady=5)
dois.grid(column=2, row=3, padx=5, pady=5)
tres.grid(column=3, row=3, padx=5, pady=5)
quatro.grid(column=1, row=2, padx=5, pady=5)
cinco.grid(column=2, row=2, padx=5, pady=5)
seis.grid(column=3, row=2, padx=5, pady=5)

janela.mainloop()