from PyQt5 import QtMultimedia
from PyQt5 import QtCore


class Music:
    def __init__(self):
        self.shoot_music = create_music("music/shoot_sound.mp3", 100)
        self.bonus_music = create_music("music/bonus_sound.mp3", 100)
        self.monsters_music = create_music("music/monsters_die_sound.mp3", 100)
        self.player_music = create_music("music/game_sound.mp3", 50)
        self.player_music.play()
        self.player_music.stateChanged.connect(self.music_continue)

    def music_continue(self):
        self.player_music.play()


def create_music(name, volume):
    """Создает музыкальный плеер"""
    content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(name))
    music = QtMultimedia.QMediaPlayer()
    music.setVolume(volume)
    music.setMedia(content)
    return music
