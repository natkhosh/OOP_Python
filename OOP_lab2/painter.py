import os

from figures import Figure, Rectangle, Ellipse, CloseFigure

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):

        painter = QPainter(self)
        reset_brush = painter.brush()

        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.magenta))
                painter.drawRect(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))

                points = []
                for point in figure.d:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    # figures = []
    # figures = [CloseFigure((50, 50), (250, 100), (350, 350), (200, 400), (30, 380), (100, 130), (50, 50))]
    figures = [Rectangle(10, 10, 200, 100), Rectangle(250, 400, 300, 50), Ellipse(220, 30, 400, 200), Ellipse(340, 300, 300, 50),
               CloseFigure((50, 50), (250, 100), (350, 350), (200, 400), (30, 380), (100, 130), (50, 50))]
    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())
