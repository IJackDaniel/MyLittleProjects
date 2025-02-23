import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QVBoxLayout, QWidget, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Даем название нашему окну.
        self.setWindowTitle("Time to hacking")
        # Задаем размеры приложения
        self.setFixedSize(QSize(400, 300))

        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Введи любой пароль"))

        inp = QLineEdit()
        inp.setMaxLength(3)
        inp.setPlaceholderText("пароль")

        inp.returnPressed.connect(self.return_pressed)  # Ввёл и нажал Enter
        inp.selectionChanged.connect(self.selection_changed)  # Выделение
        inp.textChanged.connect(self.text_changed)  # Изменение текста
        inp.textEdited.connect(self.text_edited)  #
        inp.cursorPositionChanged.connect(self.e)

        vbox.addWidget(inp)

        self.result = QLabel()
        vbox.addWidget(self.result)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def e(self):
        print("rge")


    def click(self):
        print("LOL")

    def return_pressed(self):
        print("Return pressed!")
        self.result.setText("BOOM")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
