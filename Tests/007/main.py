# Jogo da forca
from gamecontroller import GameController as GC
from player import Player as py

word = GC.save_word()
GC.clear_screen()

player = py(word)

print(word)
letter = input("Write a letter: ")
check = GC.check_letter(word, letter)

print(check)