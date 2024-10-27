from PyQt5.QtWidgets import(
    QWidget,
    QPushButton,
    QLabel,
    QApplication,
    QLineEdit,
    QTextEdit
)

class User(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Note Taking Aplication")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("font-size: 15px")


        self.edit = QTextEdit(self)
        self.edit.move(50, 20)
        self.edit.resize(300, 300)

        self.label = QLabel('                                                 ', self)
        self.label.move(170, 330)

        self.button = QPushButton("Save", self)
        self.button.move(50,350)

        self.button.clicked.connect(self.save)
        
        self.show()

    def save(self):
        matn = self.edit.toPlainText()
        if matn:
            self.label.setText("Saqlandi!!!")
            with open("File.txt", 'w') as f:
                f.write(matn)
        else:
            self.label.setText("Kechirasiz siz siz yozmadingiz!!!")
res = QApplication([])
k = User()
res.exec_()