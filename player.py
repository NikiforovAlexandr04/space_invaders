class Player:
    def __init__(self):
        self.player_x = 250

    def move_left(self):
        """Передвигает игрока влево"""
        if self.player_x > 30:
            self.player_x -= 5

    def move_right(self):
        """Передвигает игрока вправо"""
        if self.player_x < 530:
            self.player_x += 5
