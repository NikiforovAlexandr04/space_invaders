class Ufo:
    def __init__(self):
        self.ufo_x = 640
        self.ufo_y = 35
        self.can_left = True

        self.can_move = False

    def ufo_move(self):
        """Движение НЛО"""
        if self.can_move:
            if self.can_left:
                self.move_left()
            else:
                self.move_right()

    def move_right(self):
        if self.ufo_x < 640:
            self.ufo_x += 10
        else:
            self.can_left = True
            self.can_move = False

    def move_left(self):
        if self.ufo_x > -50:
            self.ufo_x -= 10
        else:
            self.can_left = False
            self.can_move = False

    def begin_left(self):
        """Отправляет НЛО на начальную левую позицию"""
        self.ufo_x = -50
        self.can_move = False

    def begin_right(self):
        """Отправляет НЛО на начальную правую позицию"""
        self.ufo_x = 640
        self.can_move = False
