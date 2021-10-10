import unittest
from player import Player
from monsters import Monsters, Monster
from shell import PlayerShell
from Ufo import Ufo
from bunkers import Bunkers
from monster_shell import MonsterShell


def initialization_game():
    all_subjects = []
    player_logic = Player()
    lives = 3
    monsters = Monsters([], all_subjects, True, True)
    score = 0
    ufo = Ufo()
    bunkers = Bunkers()

    all_subjects.append(player_logic)
    all_subjects.append(lives)
    all_subjects.append(monsters.monsters)
    all_subjects.append(score)
    all_subjects.append(ufo)
    all_subjects.append(bunkers)
    all_subjects.append(monsters)

    return all_subjects


class Tests(unittest.TestCase):
    def test_move_player(self):
        player = Player()
        player.move_left()
        move_left_1_time = player.player_x
        player.move_right()
        move_right_1_time = player.player_x
        for i in range(44):
            player.move_left()
        move_left_board = player.player_x
        player.move_left()
        check_left_board = player.player_x
        for i in range(100):
            player.move_right()
        move_right_board = player.player_x
        player.move_right()
        check_right_board = player.player_x
        self.assertEqual(move_left_1_time, 245)
        self.assertEqual(move_right_1_time, 250)
        self.assertEqual(move_left_board, 30)
        self.assertEqual(check_left_board, 30)
        self.assertEqual(move_right_board, 530)
        self.assertEqual(check_right_board, 530)

    def test_nlo(self):
        ufo = Ufo()
        ufo.can_move = True
        ufo.ufo_move()
        ufo_move_left = ufo.ufo_x
        for i in range(68):
            ufo.ufo_move()
        ufo_left_board = ufo.ufo_x
        ufo.ufo_move()
        ufo_not_move = ufo.ufo_x
        ufo.can_move = True
        ufo.ufo_move()
        ufo_move_right = ufo.ufo_x
        for i in range(68):
            ufo.ufo_move()
        ufo_right_board = ufo.ufo_x
        ufo.begin_left()
        ufo_begin_left = ufo.ufo_x
        ufo.begin_right()
        ufo_begin_right = ufo.ufo_x
        self.assertEqual(ufo_move_left, 630)
        self.assertEqual(ufo_left_board, -50)
        self.assertEqual(ufo_not_move, -50)
        self.assertEqual(ufo_move_right, -40)
        self.assertEqual(ufo_right_board, 640)
        self.assertEqual(ufo_begin_left, -50)
        self.assertEqual(ufo_begin_right, 640)

    def test_shoots(self):
        all_subjects = initialization_game()
        shell = PlayerShell(all_subjects, 0, [], [], 0, 0, 432, all_subjects[0].player_x + 16, 0, 0)
        self.assertEqual(shell.shell_x, 266)
        self.assertEqual(shell.fly_shell(0), 0)
        self.assertEqual(shell.shell_y, 429)

        shell_change = PlayerShell(all_subjects, 0, [], [], 1, 0, 432, all_subjects[0].player_x + 16, 0, 0)
        for i in range(5):
            shell_change.fly_shell(0)
        self.assertEqual(shell_change.shell_y, 417)
        self.assertEqual(shell_change.shell_x, all_subjects[0].player_x + 21)

    def test_conflict_monster(self):
        all_subjects = initialization_game()
        monsters_count_begin = len(all_subjects[2])
        shell = PlayerShell(all_subjects, 0, [], [], 0, 0, 432, all_subjects[0].player_x + 6, 0, 0)
        for i in range(80):
            shell.fly_shell(0)
        self.assertEqual(shell.shell_y, 192)

        try:
            shell.fly_shell(0)
        except AttributeError:
            pass

        self.assertEqual(monsters_count_begin - 1, len(all_subjects[6].monsters))
        self.assertEqual(shell.monsters_killed, 1)
        self.assertEqual(shell.monster_conflict.name, [3, 3])
        self.assertEqual(all_subjects[3], 10)

    def test_conflict_bunker(self):
        all_subjects = initialization_game()
        all_subjects[0].move_right()
        shells = []
        shells.append([0])
        shell = PlayerShell(all_subjects, 0, shells, [], 0, 0, 432, all_subjects[0].player_x + 16, 0, 0)
        bunker_blocks_count = len(all_subjects[5].bunkers)
        for i in range(9):
            shell.fly_shell(0)
        self.assertEqual(len(all_subjects[5].bunkers), bunker_blocks_count - 1)

        for i in range(6):
            all_subjects[0].move_right()
        shell = PlayerShell(all_subjects, 0, shells, [], 0, 0, 432, all_subjects[0].player_x + 16, 0, 0)
        for i in range(12):
            shell.fly_shell(0)
        self.assertEqual(len(all_subjects[5].bunkers), bunker_blocks_count - 2)

    def test_bonus(self):
        all_subjects = initialization_game()
        shell = PlayerShell(all_subjects, 0, [], [], 0, 0, 172, 250, 0, 0)
        try:
            shell.fly_shell(2)
        except AttributeError:
            pass
        self.assertEqual(1, len(shell.bonuses))
        self.assertEqual(1, shell.bonuses[0].number)

        for i in range(56):
            shell.bonuses[0].move_down()

        self.assertEqual(False, shell.bonuses[0].move_down())
        self.assertEqual(True, shell.bonuses[0].move_down())

    def test_monster_shoot(self):
        all_subjects = initialization_game()
        self.assertEqual(True, all_subjects[6].monsters_shoot(165, all_subjects[6].monsters))
        self.assertEqual(1, len(all_subjects[6].monsters_shell))
        self.assertEqual(1, len(all_subjects[6].monsters_shell))

        shell = all_subjects[6].monsters_shell[0]

        self.assertEqual(175, shell.monster_shell_x)
        self.assertEqual(195, shell.monster_shell_y)

        for i in range(7):
            all_subjects[2].pop()

        self.assertEqual(True, all_subjects[6].monsters_shoot(165, all_subjects[6].monsters))
        self.assertEqual(3, len(all_subjects[6].monsters_shell))

        for i in range(7):
            all_subjects[2].pop()

        self.assertEqual(True, all_subjects[6].monsters_shoot(165, all_subjects[6].monsters))
        self.assertEqual(5, len(all_subjects[6].monsters_shell))

        for i in range(7):
            all_subjects[2].pop()

        self.assertEqual(True, all_subjects[6].monsters_shoot(165, all_subjects[6].monsters))
        self.assertEqual(8, len(all_subjects[6].monsters_shell))

    def test_player_lives(self):
        all_subjects = initialization_game()
        monster_shell = MonsterShell(245, 250, [], all_subjects, 0)
        for i in range(48):
            monster_shell.move_down()

        self.assertEqual(True, monster_shell.can_move_down())
        monster_shell.move_down()

        self.assertEqual(False, monster_shell.can_move_down())
        self.assertEqual(2, all_subjects[1])


if __name__ == '__main__':
    unittest.main()
