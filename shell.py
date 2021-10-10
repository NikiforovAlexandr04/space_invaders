from math import fabs
from bonus import Bonus


class PlayerShell:
    def __init__(self, all_subjects, number, shells, bonuses, x_change, x_begin, shell_y, shell_x,
                 monsters_music, bonus_music):
        self.player = all_subjects[0]
        self.shell_x = int(shell_x) + int(x_begin)
        self.shell_y = int(shell_y)
        self.monster_conflict = 0
        self.monsters = all_subjects[2]
        self.bunkers = all_subjects[5].bunkers
        self.all_subjects = all_subjects
        self.number = int(number)
        self.shells = shells
        self.ufo = all_subjects[4]
        self.monsters_killed = 0
        self.bonuses = bonuses
        self.x_change = int(x_change)
        self.bonus_time = []
        self.bonus_time.append([3, 1])
        self.bonus_time.append([7, 1])
        self.bonus_time.append([12, 1])
        self.bonus_time.append([17, 2])
        self.bonus_time.append([22, 2])
        self.bonus_music = bonus_music
        self.monsters_music = monsters_music

    def fly_shell(self, monsters_killed):
        """Отвечает за движение снаряда"""
        self.monsters_killed = monsters_killed
        conflict_monster = self.conflict_monster()
        if self.shell_y < 640 and conflict_monster and self.conflict_bunkers() and self.ufo_conflict():
            self.shell_y -= 3
            self.shell_x += self.x_change
            return 0
        self.shells[self.number] = 0
        if not conflict_monster:
            return 1
        return 0

    def conflict_monster(self):
        """Проверяет пересечение траектории с монстрами, если пересекаются то монстр удаляется и меняются очки"""
        for monster in self.monsters:
            conflict_x = fabs(self.shell_x + 2.5 - monster.monster_x - 16) < 16
            conflict_y = fabs(self.shell_y - monster.monster_y - 12.5) < 12.5
            if conflict_x and conflict_y:
                self.monsters_killed += 1
                self.bonuses_fall(monster)
                self.monster_conflict = monster
                self.monsters.remove(monster)
                self.change_score()
                self.monsters_music.play()
                return False
        return True

    def change_score(self):
        """Меняет очки при конфликте с монстром"""
        if self.monster_conflict.name[1] == 0:
            self.all_subjects[3] += 20
        if self.monster_conflict.name[1] == 1:
            self.all_subjects[3] += 17
        if self.monster_conflict.name[1] == 2:
            self.all_subjects[3] += 13
        if self.monster_conflict.name[1] == 3:
            self.all_subjects[3] += 10

    def conflict_bunkers(self):
        """Меняет очки при конфликте с монстром"""
        for bunker in self.bunkers:
            conflict_x = fabs(self.shell_x + 2.5 - bunker.bunker_x - 3) < 3
            conflict_y = fabs(self.shell_y - bunker.bunker_y - 5) < 5
            if conflict_x and conflict_y:
                self.bunkers.remove(bunker)
                return False
        return True

    def ufo_conflict(self):
        """Проверяет пересечение траектории с НЛО, если пересекаются то НЛО убирается на начальную позицию
         и меняются очки"""
        conflict_x = fabs(self.shell_x + 2.5 - self.ufo.ufo_x - 22.5) < 22.5
        conflict_y = fabs(self.shell_y - self.ufo.ufo_y - 10) < 10
        if conflict_x and conflict_y:
            self.monsters_music.play()
            if self.ufo.can_left:
                self.ufo.begin_left()
            else:
                self.ufo.begin_right()
            self.change_ufo_score()
            return False
        return True

    def change_ufo_score(self):
        """Меняет очки при конфликте с НЛО"""
        self.all_subjects[3] += 100

    def bonuses_fall(self, monster):
        """Создает бонус"""
        for bonus_number in self.bonus_time:
            if bonus_number[1] == 1 and self.monsters_killed == bonus_number[0]:
                self.bonuses.append(Bonus(monster.monster_x, monster.monster_y, self.player, 1))
                self.bonus_music.play()
            if bonus_number[1] == 2 and self.monsters_killed == bonus_number[0]:
                self.bonuses.append(Bonus(monster.monster_x, monster.monster_y, self.player, 2))
                self.bonus_music.play()
