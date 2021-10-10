from shell import PlayerShell


class PlayerShot:
    def __init__(self, all_subjects, tick_logic, bonuses, monsters_music, bonus_music, player_shells):
        self.all_subjects = all_subjects
        self.tick_logic = tick_logic
        self.player_shells = player_shells
        self.bonuses = bonuses
        self.monsters_music = monsters_music
        self.bonus_music = bonus_music
        self.player_shells_count = 0

    def shoot(self):
        if self.tick_logic.type_shell == 1:
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, 0, 0, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
        elif self.tick_logic.type_shell == 2:
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, 0, -4, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, 0, 4, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
            self.tick_logic.type_shell = 1
        elif self.tick_logic.type_shell == 3:
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, -1, 0, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, 1, 0, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
            self.player_shells_count += 1
            self.player_shells.append(PlayerShell(self.all_subjects, self.player_shells_count - 1, self.player_shells,
                                                  self.bonuses, 0, 0, 432, self.all_subjects[0].player_x + 16,
                                                  self.monsters_music, self.bonus_music))
            self.tick_logic.type_shell = 1
