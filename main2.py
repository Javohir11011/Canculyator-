from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QPushButton,QMessageBox

class User(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setStyleSheet("font-size: 20px")

        self.setWindowTitle("Login Form")
        self.setGeometry(100, 100, 300, 300)

        self.label1 = QLabel("Username: ", self)
        self.label1.move(20, 10)

        self.edit1 = QLineEdit(self)
        self.edit1.move(20,40)

        self.label2 = QLabel("Password", self)
        self.label2.move(20, 80)

        self.edit2 = QLineEdit(self)
        self.edit2.move(20, 110)

        self.button = QPushButton("Login", self)
        self.button.move(50, 150)
        self.button.clicked.connect(self.tek)
        self.show()
    

    def tek(self):
        name = self.edit1.text()
        parol = self.edit2.text()
        if name == 'bratan' and parol == "qale":
            QMessageBox.information(self, "Succcses", "Ajoyib 'baratan'")
        else:
            QMessageBox.information(self, "Error", "jkhv")



res = QApplication([])
oyna = User()
res.exec_()