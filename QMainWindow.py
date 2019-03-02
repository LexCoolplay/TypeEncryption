import PyQt5.QtWidgets as Widgets
import PyQt5.QtCore as core
import sys


class MainWindow(Widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("myWindow")


def main():
    main_app = Widgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    main_app.exec()


if __name__ == "__main__":
    main()
