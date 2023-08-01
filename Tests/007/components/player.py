class Player:
    def __init__(self):
        self.lives  = 6
        self.score = 0

    def damage_life(life, check):
        if check == False:
            if life >= 0:
                life -= 1
                return life
            elif life == 0:
                return False
        else:
            return life
