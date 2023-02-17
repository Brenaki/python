#código criado pelo Chat GPT

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Bloco de Notas")

# Text Widget
text = tk.Text(root)
text.pack()

# Função para Salvar o arquivo
def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    if filename:
        with open(filename, "w") as f:
            text_content = text.get(1.0, "end-1c")
            f.write(text_content)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

root.mainloop()
