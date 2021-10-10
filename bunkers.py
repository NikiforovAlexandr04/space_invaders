class Bunkers:
    def __init__(self):
        self.bunkers = []
        x = 70
        for i in range(5):
            self.create_bunker(x, 400)
            x += 100

    def create_bunker(self, x, y):
        """Функция создает бункер, начинающийся в заданной координате"""
        x1 = x
        for i in range(5):
            self.bunkers.append(Bunker(x1, y))
            x1 += 6
        x1 += 12
        for i in range(5):
            self.bunkers.append(Bunker(x1, y))
            x1 += 6
        y -= 10
        x1 = x + 6
        for i in range(10):
            self.bunkers.append(Bunker(x1, y))
            x1 += 6
        y -= 10
        x1 = x + 24
        for i in range(4):
            self.bunkers.append(Bunker(x1, y))
            x1 += 6


class Bunker:
    def __init__(self, x, y):
        self.bunker_x = x
        self.bunker_y = y
