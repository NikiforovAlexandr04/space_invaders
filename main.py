import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget
from interface import ExampleWindow
from player import Player
from monsters import Monsters
from shell import PlayerShell
from Ufo import Ufo
from bunkers import Bunkers
from PyQt5 import QtMultimedia
from tick import Tick
from player_shot import PlayerShot
from scores import Scores
from music_logic import Music
from save_logic import SaveGame


class Logic(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        """Инициализируются все объекты игры, создаются таймеры для переотрисовки и запрещения нажатия на пробел"""
        self.all_subjects = []
        self.player_logic = Player()
        self.lives = 3
        self.monsters_shell = []
        self.monsters = Monsters(self.monsters_shell, self.all_subjects, True, True)
        self.score = 0
        self.ufo = Ufo()
        self.bunkers = Bunkers()
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.tick)
        self.update_timer.start(30)
        self.scores = []
        self.bonuses = []
        self.monsters_shell_count = 0

        self.all_subjects.append(self.player_logic)
        self.all_subjects.append(self.lives)
        self.all_subjects.append(self.monsters.monsters)
        self.all_subjects.append(self.score)
        self.all_subjects.append(self.ufo)
        self.all_subjects.append(self.bunkers)

        self.can_shoot = True
        self.is_pause = False
        self.table_show = False

        self.tick_count = 0
        self.top_scores = 0
        self.tick_for_space = 0
        self.monsters_speed = 20
        self.type_shell = 1

        self.music_logic = Music()

        self.tick_logic = Tick(self.bonuses, self.type_shell, self.monsters)
        self.score_logic = Scores(self.all_subjects[3])
        self.player_shot = PlayerShot(self.all_subjects, self.tick_logic, self.bonuses, self.music_logic.monsters_music,
                                      self.music_logic.bonus_music, [])
        self.interface = ExampleWindow(self, self.all_subjects, self.monsters.monsters_shell, self.monsters.
                                       monsters[0].monster_y, self.player_shot.player_shells, self.table_show,
                                       self.scores, self.bonuses)

    def tick(self):
        """Функция занимается переотрисовкой интерфейса"""
        self.tick_count += 1
        self.tick_for_space += 1
        self.tick_logic.allow_monsters_shoot += 1

        if self.tick_count % 50:
            self.tick_logic.bonus_fall()

        if self.tick_logic.allow_monsters_shoot % 70 == 0:
            self.tick_logic.monsters_can_shoot = True

        if len(self.all_subjects[2]) == 0:
            self.upgrade_level()

        self.tick_logic.find_low_monster()

        self.tick_logic.move_player_shells(self.player_shot.player_shells)

        self.tick_logic.can_monsters_shoot(self.player_logic, self.all_subjects[2])

        if self.tick_count % 2 == 0:
            self.tick_logic.move_monsters_shells()

        if self.tick_count % self.monsters_speed == 0:
            self.monsters.monsters_move()

        if self.tick_for_space % 70 == 0:
            self.can_shoot = True

        if self.tick_count % 15 == 0:
            self.ufo.ufo_move()

        if self.tick_count % 500 == 0:
            self.ufo.can_move = True

        if self.tick_logic.low_monster.monster_y > 350 or self.all_subjects[1] == 0:
            self.score_logic.print_score(self.all_subjects[3])
            self.update_timer.stop()

        self.interface = ExampleWindow(self, self.all_subjects, self.monsters.monsters_shell,
                                       self.tick_logic.low_monster.monster_y,
                                       self.player_shot.player_shells,  self.table_show, self.scores, self.bonuses)

    def stop_update(self):
        """станавливается таймер игры"""
        self.update_timer.stop()

    def keyPressEvent(self, event):
        """Функция обрабатывает нажатие на клавиатуру"""
        if event.key() == QtCore.Qt.Key_P:
            self.make_pause()

        if not self.is_pause:
            if event.key() == QtCore.Qt.Key_T:
                self.show_table()

            if event.key() == QtCore.Qt.Key_R:
                self.score_logic.print_score(self.all_subjects[3])
                self.reboot()

            if event.key() == QtCore.Qt.Key_A:
                self.all_subjects[0].move_left()

            if event.key() == QtCore.Qt.Key_D:
                self.all_subjects[0].move_right()

            if event.key() == QtCore.Qt.Key_Space:
                self.shot()

            if event.key() == QtCore.Qt.Key_S:
                save = SaveGame(self.all_subjects, self.tick_logic.monster_kill, self.tick_logic.allow_monsters_shoot,
                                self.tick_count, self.tick_for_space, self.monsters_speed, self.player_shot.
                                player_shells_count, self.can_shoot, self.ufo, self.player_shot.player_shells,
                                self.monsters.monsters_shell, self.monsters, self.bunkers, self.bonuses,
                                self.music_logic.monsters_music, self.music_logic.bonus_music)
                save.save_game()

            if event.key() == QtCore.Qt.Key_F:
                self.reload_game()
        event.accept()

    def allow_shoot(self):
        """Функция разрешает выстрел"""
        self.can_shoot = True

    def reboot(self):
        """Перезапускает игру"""
        self.all_subjects = []
        self.player_logic = Player()
        self.lives = 3
        self.monsters_shell = []
        self.monsters = Monsters(self.monsters_shell, self.all_subjects, True, True)
        self.score = 0
        self.ufo = Ufo()
        self.bunkers = Bunkers()
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.tick)
        self.update_timer.start(30)
        self.scores = []
        self.bonuses = []

        self.all_subjects.append(self.player_logic)
        self.all_subjects.append(self.lives)
        self.all_subjects.append(self.monsters.monsters)
        self.all_subjects.append(self.score)
        self.all_subjects.append(self.ufo)
        self.all_subjects.append(self.bunkers)

        self.can_shoot = True
        self.is_pause = False
        self.table_show = False

        self.tick_count = 0
        self.top_scores = 0
        self.tick_for_space = 0
        self.monsters_speed = 50
        self.type_shell = 1

        self.music_logic = Music()

        self.tick_logic = Tick(self.bonuses, self.type_shell, self.monsters)
        self.score_logic = Scores(self.all_subjects[3])
        self.player_shot = PlayerShot(self.all_subjects, self.tick_logic, self.bonuses, self.music_logic.
                                      monsters_music, self.music_logic.bonus_music, [])

        self.interface = ExampleWindow(self, self.all_subjects, self.monsters.monsters_shell, self.monsters.monsters[0].
                                       monster_y, self.player_shot.player_shells, self.table_show, self.scores,
                                       self.bonuses)

    def upgrade_level(self):
        self.tick_logic.monster_killed = 0
        self.monsters_shell = self.monsters.monsters_shell
        self.monsters = Monsters(self.monsters_shell, self.all_subjects, True, True)
        self.all_subjects[2] = self.monsters.monsters
        if self.monsters_speed > 9:
            self.monsters_speed -= 5

    def make_pause(self):
        if not self.is_pause:
            self.update_timer.stop()
            self.is_pause = True
        else:
            self.update_timer.start(30)
            self.is_pause = False

    def show_table(self):
        if not self.table_show:
            self.update_timer.stop()
            self.scores = self.score_logic.show_scores()
            self.table_show = True
            self.interface = ExampleWindow(self, self.all_subjects, self.monsters.monsters_shell, 0,
                                           self.player_shot.player_shells, self.table_show, self.scores, self.bonuses)
        else:
            self.update_timer.start(30)
            self.table_show = False

    def shot(self):
        if self.can_shoot:
            self.music_logic.shoot_music.play()
            self.player_shot.shoot()
            self.can_shoot = False
            self.tick_for_space = 0

    def reload_game(self):
        save = SaveGame(self.all_subjects, self.tick_logic.monster_kill, self.tick_logic.allow_monsters_shoot,
                        self.tick_count, self.tick_for_space, self.monsters_speed,
                        self.player_shot.player_shells_count, self.can_shoot, self.ufo,
                        self.player_shot.player_shells, self.monsters.monsters_shell, self.monsters, self.bunkers,
                        self.bonuses, self.music_logic.monsters_music, self.music_logic.bonus_music)
        save.load_game()
        self.all_subjects = save.all_subjects
        self.tick_logic.monster_kill = save.monster_kill
        self.tick_logic.allow_monsters_shoot = save.allow_monster_shoot
        self.tick_count = save.tick_count
        self.tick_for_space = save.tick_for_space
        self.monsters_speed = save.monster_speed
        self.can_shoot = save.can_shoot
        self.monsters = Monsters(self.monsters_shell, self.all_subjects, save.monsters_can_left, save.monsters_can_down)
        self.monsters.monsters = save.monsters_reload
        self.all_subjects[2] = self.monsters.monsters
        self.monsters.monsters_shell = save.reload_shells_monster
        self.bunkers = save.bunkers
        self.bonuses = save.bonuses
        self.tick_logic = Tick(self.bonuses, self.type_shell, self.monsters)
        self.score_logic = Scores(self.all_subjects[3])
        self.player_shot = PlayerShot(self.all_subjects, self.tick_logic, self.bonuses, self.music_logic.monsters_music,
                                      self.music_logic.bonus_music, save.reload_shells_player)
        self.player_shot.player_shells_count = save.player_shells_count


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = Logic()
    game.show()
    sys.exit(app.exec_())