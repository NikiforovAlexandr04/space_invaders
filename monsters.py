from PyQt5 import QtCore
from monster_shell import MonsterShell
from math import fabs


class Monsters:
    def __init__(self, monsters_shell, all_subjects, can_left, can_down):
        self.all_subjects = all_subjects
        self.monsters_shell = monsters_shell
        self.monsters = []
        x = 130
        y = 80
        for i in range(4):
            x_1 = x
            for j in range(7):
                self.monsters.append(Monster(x_1, y, [j, i]))
                x_1 += 40
            y += 30
        self.can_left = can_left
        self.can_down = can_down
        self.monsters_for_shell = []

    def monsters_move(self):
        """Функция занимается движением монстров"""
        extreme_monsters = self.find_monsters()
        left_monster = extreme_monsters[0]
        right_monster = extreme_monsters[1]
        if self.can_left and left_monster.monster_x > 30:
            for monster in self.monsters:
                monster.move_left()
        elif self.can_down:
            self.can_left = False
            for monster in self.monsters:
                monster.move_down()
            self.can_down = False
        elif right_monster.monster_x < 530:
            for monster in self.monsters:
                monster.move_right()
        else:
            for monster in self.monsters:
                monster.move_down()
            self.can_left = True
            self.can_down = True

    def monsters_shoot(self, player_x, all_monsters):
        """Функция отвечает за выстрел монстров"""
        monsters_for_shell = monsters_for_shoot(all_monsters)
        for monsters in monsters_for_shell:
            if len(monsters) > 0:
                low_monster = monsters[len(monsters) - 1]
                if fabs(low_monster.monster_x - player_x - 15) < 15:
                    if low_monster.name[1] == 3 or low_monster.name[1] == 0:
                        self.monsters_shell.append(MonsterShell(player_x, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, 0))
                    if low_monster.name[1] == 0:
                        self.monsters_shell.append(MonsterShell(player_x, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, -2))
                        self.monsters_shell.append(MonsterShell(player_x, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell,self.all_subjects, 2))
                    if low_monster.name[1] == 1:
                        self.monsters_shell.append(MonsterShell(player_x, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, -2))
                        self.monsters_shell.append(MonsterShell(player_x, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, 2))
                    if low_monster.name[1] == 2:
                        self.monsters_shell.append(MonsterShell(player_x - 5, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, 0))
                        self.monsters_shell.append(MonsterShell(player_x + 5, monsters[len(monsters) - 1].monster_y,
                                                                self.monsters_shell, self.all_subjects, 0))
                    return True
        return False

    def find_monsters(self):
        """Наъодит самого правого и самого левого монстра"""
        min_number = 10
        left_monster = 0
        max_number = -1
        right_monster = 0
        for monster in self.monsters:
            if monster.name[0] < min_number:
                min_number = monster.name[0]
                left_monster = monster
            if monster.name[0] > max_number:
                max_number = monster.name[0]
                right_monster = monster
        return [left_monster, right_monster]


def monsters_for_shoot(all_monsters):
    """Распределет монстров по группам для стрельбы"""
    monsters_for_shell = []
    for i in range(7):
        monsters = []
        monsters_for_shell.append(monsters)
    for monster in all_monsters:
        if monster.name[0] == 0:
            monsters_for_shell[0].append(monster)
        if monster.name[0] == 1:
            monsters_for_shell[1].append(monster)
        if monster.name[0] == 2:
            monsters_for_shell[2].append(monster)
        if monster.name[0] == 3:
            monsters_for_shell[3].append(monster)
        if monster.name[0] == 4:
            monsters_for_shell[4].append(monster)
        if monster.name[0] == 5:
            monsters_for_shell[5].append(monster)
        if monster.name[0] == 6:
            monsters_for_shell[6].append(monster)
    return monsters_for_shell


class Monster:
    def __init__(self, x, y, name):
        self.name = name
        self.monster_x = x
        self.monster_y = y

    def move_left(self):
        self.monster_x -= 10

    def move_right(self):
        self.monster_x += 10

    def move_down(self):
        self.monster_y += 30
