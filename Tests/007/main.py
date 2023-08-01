# Jogo da forca
from gamecontroller import GameController as GC
from player import Player as py


word, life = GC().word, GC().life
GC.clear_screen()

print(word)
letter = input("Write a letter: ")
check = GC.check_letter(word, letter)
life_check = py.damage_life(life, check)

if life_check == False:
    GC.game_over()

print(check)
print(life_check)