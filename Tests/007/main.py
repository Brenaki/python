# Jogo da forca
from components.gamecontroller import GameController as GC
from components.player import Player

word = GC(GC.choose_word()).word
lives = Player().lives
GC.clear_screen()
print(word)

letter = input("Write a letter: ")
check = GC.check_letter(word, letter)
life_check = Player.damage_life(lives, check)
if life_check == False:
    GC.game_over()

print(check)
print(life_check)