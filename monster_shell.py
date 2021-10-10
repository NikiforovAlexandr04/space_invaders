from math import fabs


class MonsterShell:
    def __init__(self, x, y, monsters_shell, all_subjects, change_x):
        self.monster_shell_x = x + 10
        self.monster_shell_y = y + 25
        self.monsters_shell = monsters_shell
        self.change_x = change_x
        self.all_subjects = all_subjects

    def can_move_down(self):
        """Функция занимается движением снаряда"""
        return self.monster_shell_y < 500 and self.conflict_player() and self.conflict_bunker()

    def move_down(self):
        self.monster_shell_y += 3
        self.monster_shell_x += self.change_x

    def conflict_player(self):
        """Функция проверяет пересекаются лм траектории снаряда и игрока, ели да то у игрока уменьшаются жизни"""
        conflict_x = fabs(self.monster_shell_x + 2.5 - self.all_subjects[0].player_x - 20.5) < 20.5
        conflict_y = fabs(435.5 - self.monster_shell_y) < 15.5
        if conflict_y and conflict_x:
            self.all_subjects[1] -= 1
            return False
        return True

    def conflict_bunker(self):
        """Функция проверяет пересекаются лм траектории снаряда и бункер, ели да то бункер удаляется"""
        for bunker in self.all_subjects[5].bunkers:
            conflict_x = fabs(self.monster_shell_x + 2.5 - bunker.bunker_x - 3) < 3
            conflict_y = fabs(bunker.bunker_y - self.monster_shell_y - 5) < 5
            if conflict_y and conflict_x:
                self.all_subjects[5].bunkers.remove(bunker)
                return False
        return True
