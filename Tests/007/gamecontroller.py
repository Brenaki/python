from player import Player as py

class GameController:
    def __init__(self):
        self.word = GameController.save_word()
        self.player = py(self.word)

    def save_word():
        word = GameController.choose_word()
        return word

    def clear_screen():
        import os 
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_word():
        # Read words.txt
        with open("words.txt", "r") as file:
            words = file.readlines()

        # Random Number generator
        import random as rm
        word = rm.randrange(0, len(words))

        # Choose word
        forca = words[word]

        # Close words.txt
        file.close()

        # Return word
        return forca
    
    def check_letter(word, letter):
        letter = letter.lower()
        for i in range(len(word)):
            if word[i] == letter:
                return True
        return False