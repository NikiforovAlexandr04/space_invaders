from math import fabs


class Bonus:
    def __init__(self, x, y, player, number):
        self.bonus_x = x + 15
        self.bonus_y = y
        self.player = player
        self.number = number

    def move_down(self):
        """Бонус падает вниз"""
        if self.conflict_player():
            if self.bonus_y < 460:
                self.bonus_y += 5
            return False
        return True

    def conflict_player(self):
        """Проверяет пересекаются ли игрок и бонус"""
        conflict_x = fabs(self.bonus_x - self.player.player_x - 16) < 16
        conflict_y = fabs(self.bonus_y - 450 - 13) < 13
        if conflict_x and conflict_y:
            return False
        return True
