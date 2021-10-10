class Tick:
    def __init__(self, bonuses, type_shell, monsters):
        self.bonuses = bonuses
        self.type_shell = type_shell
        self.monsters = monsters
        self.low_monster = 0
        self.monster_kill = 0
        self.monsters_can_shoot = True
        self.allow_monsters_shoot = 0

    def bonus_fall(self):
        for bonus in self.bonuses:
            if bonus.move_down():
                if bonus.number == 1:
                    self.bonuses.remove(bonus)
                    self.type_shell = 2
                if bonus.number == 2:
                    self.bonuses.remove(bonus)
                    self.type_shell = 3

    def find_low_monster(self):
        number = 0
        for monster in self.monsters.monsters:
            if monster.name[1] >= number:
                self.low_monster = monster
                number = monster.name[1]

    def move_player_shells(self, player_shells):
        for shell in player_shells:
            if shell != 0:
                self.monster_kill += shell.fly_shell(self.monster_kill)

    def move_monsters_shells(self):
        i = -1
        for shell in self.monsters.monsters_shell:
            i += 1
            if shell != 0:
                if shell.can_move_down():
                    shell.move_down()
                else:
                    self.monsters.monsters_shell[i] = 0

    def can_monsters_shoot(self, player, monsters):
        if self.monsters_can_shoot:
            if self.monsters.monsters_shoot(player.player_x, monsters):
                self.monsters_can_shoot = False
                self.allow_monsters_shoot = 0
