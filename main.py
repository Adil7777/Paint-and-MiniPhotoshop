from Paint import Paint
from mini_photoshop import MiniPhotoshop
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        TITLLE = 'Проект'
        TOP = 400  # Координаты левого верхнего угла
        LEFT = 400
        WIDTH = 400  # Размеры окна
        HEIGHT = 400

        self.setWindowTitle(TITLLE)
        self.setGeometry(TOP, LEFT, WIDTH, HEIGHT)

        self.paint = QPushButton('Paint', self)
        self.paint.resize(100, 100)
        self.paint.move(100, 100)
        self.paint.clicked.connect(self.paint_)

        self.a = Paint()
        self.b = MiniPhotoshop()

        self.mini_photos = QPushButton('Mini Photoshop', self)
        self.mini_photos.resize(100, 100)
        self.mini_photos.move(200, 100)
        self.mini_photos.clicked.connect(self.mini_photos_)

    def paint_(self):
        self.a.show()
        self.hide()

    def mini_photos_(self):
        self.b.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
