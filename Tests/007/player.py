class Player:
    def damage_life(life, check):
        if check == False:
            if life >= 0:
                life -= 1
                return life
            elif life == 0:
                return False
        else:
            return life