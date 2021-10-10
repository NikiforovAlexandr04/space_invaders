import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QTableWidget
from PyQt5.QtCore import QSize
from numbers import Number


class ExampleWindow:
    def __init__(self, MainWindow, all_subjects, monsters_shell, low_monster_y, player_shells, table_show,
                 scores, bonuses):
        super(ExampleWindow, self).__init__()
        self.main_window = MainWindow
        self.main_window.setWindowTitle("Space_invaders")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.main_window.setObjectName("MainWindow")
        self.main_window.setFixedSize(600, 640)
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(0, 0, 600, 640)
        self.image_label.setPixmap(QtGui.QPixmap("pictures/space.jpg"))
        self.image_label.setScaledContents(True)

        self.centralwidget.setObjectName("centralwidget")

        self.player = all_subjects[0]
        self.lives = all_subjects[1]
        self.monsters = all_subjects[2]
        self.scores = str(all_subjects[3])
        self.bunkers = all_subjects[5]
        self.ufo = all_subjects[4]

        self.monsters_shell = monsters_shell
        self.player_shells = player_shells
        self.bonuses = bonuses

        if table_show:
            self.scores_table = ""
            self.table_score = QTableWidget(self.centralwidget)
            self.table_score.setGeometry(QtCore.QRect(150, 150, 300, 350))
            self.table_score.setRowCount(10)
            self.table_score.setColumnCount(1)
            self.table_score.setHorizontalHeaderLabels(('Best scores', ''))
            i = -2
            for score in scores:
                i += 1
                item = QtWidgets.QTableWidgetItem(str(score))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.table_score.setItem(i, 1, item)
                self.table_score.setColumnWidth(i, 265)
        elif low_monster_y < 350 and self.lives != 0:
            self.create_ufo(self.ufo)
            self.create_monsters(self.monsters)
            self.create_player(self.player.player_x, 450)

            self.line = QtWidgets.QFrame(self.centralwidget)
            self.line.setGeometry(QtCore.QRect(0, 510, 600, 16))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")

            self.Live1 = QLabel(self.centralwidget)
            self.Live1.setGeometry(QtCore.QRect(30, 550, 41, 31))
            self.Live1.setPixmap(QtGui.QPixmap("pictures/player.jpg"))
            self.Live1.setObjectName("Live1")

            if self.lives > 1:
                self.Live2 = QLabel(self.centralwidget)
                self.Live2.setGeometry(QtCore.QRect(70, 550, 41, 31))
                self.Live2.setPixmap(QtGui.QPixmap("pictures/player.jpg"))
                self.Live2.setObjectName("Live2")

            if self.lives > 2:
                self.Live3 = QLabel(self.centralwidget)
                self.Live3.setGeometry(QtCore.QRect(110, 550, 41, 31))
                self.Live3.setPixmap(QtGui.QPixmap("pictures/player.jpg"))
                self.Live3.setObjectName("Live3")

            self.score = QtWidgets.QLineEdit(self.centralwidget)
            self.score.setGeometry(QtCore.QRect(400, 540, 150, 50))
            self.score.setReadOnly(True)
            self.score.setText(self.scores)
            self.score.setStyleSheet("color: rgb(28, 143, 255); font-size: 30px;")

            self.create_bunkers(self.bunkers)

            for shell in self.player_shells:
                if not isinstance(shell, Number):
                    self.create_player_shell(shell.shell_x, shell.shell_y)

            for shell in self.monsters_shell:
                if shell != 0:
                    self.create_monsters_shell(shell)

            for bonus in self.bonuses:
                self.bonus_create(bonus)
        else:
            self.widget = QtWidgets.QLineEdit(self.centralwidget)
            self.widget.setGeometry(QtCore.QRect(100, 200, 350, 100))
            self.widget.setReadOnly(True)
            self.widget.setStyleSheet("color: rgb(28, 143, 255); font-size: 30px;")
            self.widget.setText("You lose, your score:" + ' ' + self.scores)

        self.main_window.setCentralWidget(self.centralwidget)

    def create_monsters(self, monsters):
        """Функция занимается отрисовкой монстров"""
        for monster in monsters:
            monster_interface = QLabel(self.centralwidget)
            if monster.name[1] == 0:
                monster_interface.setPixmap(QtGui.QPixmap("pictures/monster5.jpg"))
            if monster.name[1] == 1:
                monster_interface.setPixmap(QtGui.QPixmap("pictures/monster1.jpg"))
            if monster.name[1] == 2:
                monster_interface.setPixmap(QtGui.QPixmap("pictures/monster2.jpg"))
            if monster.name[1] == 3:
                monster_interface.setPixmap(QtGui.QPixmap("pictures/monster4.jpg"))
            monster_interface.setScaledContents(True)
            monster_interface.setGeometry(QtCore.QRect(monster.monster_x, monster.monster_y, 32, 25))

    def create_player(self, x, y):
        """Функция занимается отрисовкой игрока"""
        self.player = QLabel(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(x, y, 41, 31))
        self.player.setPixmap(QtGui.QPixmap("pictures/player.jpg"))
        self.player.setObjectName("player")

    def create_player_shell(self, x, y):
        """Функция занимается отрисовкой снарядов игрока"""
        shell = QLabel(self.centralwidget)
        shell.setGeometry(QtCore.QRect(x, y, 5, 12))
        shell.setScaledContents(True)
        shell.setPixmap(QtGui.QPixmap("pictures/player_shell.jpg"))

    def create_ufo(self, ufo):
        """Функция занимается отрисовкой НЛО"""
        ufo_ = QLabel(self.centralwidget)
        ufo_.setGeometry(QtCore.QRect(ufo.ufo_x, ufo.ufo_y, 45, 20))
        ufo_.setScaledContents(True)
        ufo_.setPixmap(QtGui.QPixmap("pictures/NLO.jpg"))

    def create_bunkers(self, bunkers):
        """Функция занимается отрисовкой бункеров"""
        for bunker in bunkers.bunkers:
            bunker_interface = QLabel(self.centralwidget)
            bunker_interface.setGeometry(QtCore.QRect(bunker.bunker_x, bunker.bunker_y, 6, 10))
            bunker_interface.setScaledContents(True)
            bunker_interface.setPixmap(QtGui.QPixmap("pictures/bunkers.jpg"))

    def create_monsters_shell(self, shell):
        """Функция занимается отрисовкой снарядов монстров"""
        shell_ = QLabel(self.centralwidget)
        shell_.setGeometry(QtCore.QRect(shell.monster_shell_x, shell.monster_shell_y, 5, 12))
        shell_.setScaledContents(True)
        shell_.setPixmap(QtGui.QPixmap("pictures/monster_shell.jpg"))

    def bonus_create(self, bonus):
        bonus_ = QLabel(self.centralwidget)
        bonus_.setGeometry(QtCore.QRect(bonus.bonus_x, bonus.bonus_y, 12, 15))
        bonus_.setScaledContents(True)
        bonus_.setPixmap(QtGui.QPixmap("pictures/bonus.jpg"))
