import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Window")
        self.setGeometry(100, 100, 600, 400)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 200, 30)

        self.button = QPushButton('Click Me', self)
        self.button.setGeometry(50, 100, 100, 30)
        self.button.clicked.connect(self.on_click)

        self.button = QPushButton('Close', self)
        self.button.setGeometry(175, 100, 100, 30)
        self.button.clicked.connect(self.close)

    def on_click(self):
        text = self.textbox.text()
        self.textbox.setText("Hello " + text)   
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())