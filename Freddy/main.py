from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QMovie
import pygame
import sys

pygame.mixer.init()
song = pygame.mixer.Sound("fnaf_song.mp3")
pygame.mixer.find_channel().play(song, loops=-1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 600, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("no way")

        label = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        movie = QMovie('freddy.gif')
        movie2 = QMovie('freddy2.gif')
        movie3 = QMovie('freddy3.gif')
        movie4 = QMovie('purple_guy.gif')

        label.setMovie(movie)
        label2.setMovie(movie2)
        label3.setMovie(movie3)
        label4.setMovie(movie4)

        label2.setGeometry(300, 0, 300, 300)
        label.setGeometry(0, 0, 300, 300)
        label3.setGeometry(0, 300, 300, 300)
        label4.setGeometry(300, 300, 300, 300)

        label2.setScaledContents(True)
        label.setScaledContents(True)
        label3.setScaledContents(True)
        label4.setScaledContents(True)

        movie2.start()
        movie.start()
        movie3.start()
        movie4.start()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


