from shell import PlayerShell
from monster_shell import MonsterShell
from monsters import Monsters, Monster
from bunkers import Bunkers, Bunker
from bonus import Bonus


class SaveGame:
    def __init__(self, all_subjects, monster_kill, allow_monster_shoot, tick_count, tick_for_space, monster_speed,
                 player_shells_count, can_shoot, ufo, player_shells, monsters_shells, monsters, bunkers, bonuses,
                 monsters_music, bonus_music):
        self.all_subjects = all_subjects
        self.monster_kill = monster_kill
        self.allow_monster_shoot = allow_monster_shoot
        self.tick_count = tick_count
        self.tick_for_space = tick_for_space
        self.monster_speed = monster_speed
        self.player_shells_count = player_shells_count
        self.can_shoot = can_shoot
        self.ufo = ufo
        self.player_shells = player_shells
        self.monsters_shells = monsters_shells
        self.monsters = monsters
        self.bunkers = bunkers
        self.save_game_lines = []
        self.bonuses = bonuses
        self.free_lines = []
        self.reload_shells_player = []
        self.monsters_music = monsters_music
        self.bonuses_music = bonus_music
        self.reload_shells_monster = []
        self.monsters_reload = []
        self.monsters_can_left = True
        self.monsters_can_down = True

    def save_game(self):
        game_file = open('save_game.txt', 'w')
        game_file.truncate()
        game_file.write(str(self.all_subjects[0].player_x) + "\n")
        game_file.write(str(self.all_subjects[1]) + "\n")
        game_file.write(str(self.all_subjects[3]) + "\n")
        game_file.write(str(self.monster_kill) + "\n")
        game_file.write(str(self.allow_monster_shoot) + "\n")
        game_file.write(str(self.tick_count) + "\n")
        game_file.write(str(self.tick_for_space) + "\n")
        game_file.write(str(self.monster_speed) + "\n")
        game_file.write(str(self.player_shells_count) + "\n")
        game_file.write(str(self.can_shoot) + "\n")
        game_file.write(str(self.ufo.ufo_x) + " " + str(self.ufo.ufo_y) + " " + str(self.ufo.can_left) +
                        " " + str(self.ufo.can_move) + "\n")
        game_file.write("\n")
        self.save_shells(game_file)
        self.save_monsters_bunkers_bonuses(game_file)
        game_file.close()

    def save_shells(self, game_file):
        for shell in self.player_shells:
            if shell == 0:
                game_file.write(str(shell) + "\n")
            else:
                game_file.write(str(shell.shell_x) + " " + str(shell.shell_y) + " " + str(shell.x_change) + "\n")
        game_file.write("\n")
        for shell in self.monsters_shells:
            if shell != 0:
                game_file.write(str(shell.monster_shell_x) + " " + str(shell.monster_shell_y) + " " +
                                str(shell.change_x) + "\n")
        game_file.write("\n")

    def save_monsters_bunkers_bonuses(self, game_file):
        game_file.write(str(self.monsters.can_down) + " " + str(self.monsters.can_left) + "\n")
        game_file.write("\n")
        for monster in self.monsters.monsters:
            game_file.write(str(monster.monster_x) + " " + str(monster.monster_y) + " " + str(monster.name[0]) + " " +
                            str(monster.name[1]) + "\n")
        game_file.write("\n")

        for bunker in self.bunkers.bunkers:
            game_file.write(str(bunker.bunker_x) + " " + str(bunker.bunker_y) + "\n")
        game_file.write("\n")

        for bonus in self.bonuses:
            game_file.write(str(bonus.bonus_x) + " " + str(bonus.bonus_y) + " " + str(bonus.number) + "\n")
            print(bonus.number)
        game_file.write("\n")

    def load_game(self):
        game_file = open('save_game.txt', 'r')
        for line in game_file:
            self.save_game_lines.append(line)

        self.find_full_lines()

        self.reload_all_subjects()

        self.reload_important_game_things()

        self.reload_monsters()

        self.reload_player_shell()

        self.reload_monsters_shells()

        self.reload_bunkers_bonuses()

    def find_full_lines(self):
        for i in range(len(self.save_game_lines)):
            if self.save_game_lines[i] == "\n":
                self.free_lines.append(i)

    def reload_important_game_things(self):
        self.monster_kill = int(self.save_game_lines[3])
        self.allow_monster_shoot = bool(self.save_game_lines[4])
        self.tick_count = int(self.save_game_lines[5])
        self.tick_for_space = int(self.save_game_lines[6])
        self.monster_speed = int(self.save_game_lines[7])
        self.player_shells_count = int(self.save_game_lines[8])
        self.can_shoot = bool(self.save_game_lines[9])

    def reload_all_subjects(self):
        self.all_subjects[0].player_x = int(self.save_game_lines[0])
        self.all_subjects[1] = int(self.save_game_lines[1])
        self.all_subjects[3] = int(self.save_game_lines[2])
        ufo = self.save_game_lines[10].split(" ")
        self.all_subjects[4].ufo_x = int(ufo[0])
        self.all_subjects[4].ufo_y = int(ufo[1])
        self.all_subjects[4].can_left = bool(ufo[2])
        self.all_subjects[4].can_move = bool(ufo[3])

    def reload_player_shell(self):
        count = 0
        for line in self.save_game_lines[self.free_lines[0] + 1:self.free_lines[1]]:
            count += 1
            line = line.split(" ")
            if len(line) == 1:
                self.reload_shells_player.append(0)
            else:
                self.reload_shells_player.append(PlayerShell(self.all_subjects, count - 1, self.reload_shells_player,
                                                             self.bonuses, int(line[2]), 0, int(line[1]), int(line[0]),
                                                             self.monsters_music, self.bonuses_music))

    def reload_monsters_shells(self):
        for line in self.save_game_lines[self.free_lines[1] + 1:self.free_lines[2]]:
            line = line.split(" ")
            self.reload_shells_monster.append(MonsterShell(int(line[0]), int(line[1]), self.reload_shells_monster,
                                                           self.all_subjects, int(line[2])))

    def reload_monsters(self):
        for line in self.save_game_lines[self.free_lines[2] + 1:self.free_lines[3]]:
            line = line.split(" ")
            if str(line[0]) == 'False':
                self.monsters_can_left = False
            if line[1][0] == 'F':
                self.monsters_can_down = False

        self.monsters_reload = []
        for line in self.save_game_lines[self.free_lines[3] + 1:self.free_lines[4]]:
            line = line.split(" ")
            self.monsters_reload.append(Monster(int(line[0]), int(line[1]), [int(line[2]), int(line[3])]))
        self.all_subjects[2] = self.monsters_reload

    def reload_bunkers_bonuses(self):
        self.bunkers = Bunkers()
        self.bunkers.bunkers = []
        for line in self.save_game_lines[self.free_lines[4] + 1:self.free_lines[5]]:
            line = line.split(" ")
            self.bunkers.bunkers.append(Bunker(int(line[0]), int(line[1])))
        self.all_subjects[5] = self.bunkers

        self.bonuses = []
        for line in self.save_game_lines[self.free_lines[5] + 1:self.free_lines[6]]:
            line = line.split(" ")
            self.bonuses.append(Bonus(int(line[0]), int(line[1]), self.all_subjects[0], int(line[2])))
