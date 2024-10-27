from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
)


class Kanculyator(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet("font-size: 40px")
        self.setFixedSize(400,400)
        self.setWindowTitle("--> Kankulyator <--")

        self.matn = ""
        self.v_box = QVBoxLayout()

        self.first = QHBoxLayout()
        self.birinchi_qator = QHBoxLayout()
        self.ikkinchi_qator = QHBoxLayout()
        self.uchinchi_qator = QHBoxLayout()
        self.tortinchi_qator = QHBoxLayout()
        self.beshinchi_qator = QHBoxLayout()

        self.edit = QLineEdit()

        self.first.addWidget(self.edit)

        self.qavs2 = QPushButton(")")
        self.but_bol = QPushButton("/")
        self.clear = QPushButton("C")
        self.qavs1 = QPushButton("(")

        self.clear.setStyleSheet("background-color: red; color: white")
        self.qavs1.setStyleSheet("background-color: blue; color: white")
        self.qavs2.setStyleSheet("background-color: blue; color: white")
        self.but_bol.setStyleSheet("background-color: bleak; color: white")

        self.birinchi_qator.addWidget(self.clear)
        self.birinchi_qator.addWidget(self.qavs1)
        self.birinchi_qator.addWidget(self.qavs2)
        self.birinchi_qator.addWidget(self.but_bol)

        self.but7 = QPushButton("7")
        self.but8 = QPushButton("8")
        self.but9 = QPushButton("9")
        self.but_kop = QPushButton("*")

        self.but7.setStyleSheet("background-color: green; color: white")
        self.but8.setStyleSheet("background-color: green; color: white")
        self.but9.setStyleSheet("background-color: green; color: white")
        self.but_kop.setStyleSheet("background-color: bleak; color: white")

        self.ikkinchi_qator.addWidget(self.but9)
        self.ikkinchi_qator.addWidget(self.but8)
        self.ikkinchi_qator.addWidget(self.but7)
        self.ikkinchi_qator.addWidget(self.but_kop)

        self.but4 = QPushButton("4")
        self.but5 = QPushButton("5")
        self.but6 = QPushButton("6")
        self.but_minus = QPushButton("-")

        self.but4.setStyleSheet("background-color: green; color: white")
        self.but5.setStyleSheet("background-color: green; color: white")
        self.but6.setStyleSheet("background-color: green; color: white")
        self.but_minus.setStyleSheet("background-color: bleak; color: white")

        self.uchinchi_qator.addWidget(self.but6)
        self.uchinchi_qator.addWidget(self.but5)
        self.uchinchi_qator.addWidget(self.but4)
        self.uchinchi_qator.addWidget(self.but_minus)

        self.but1 = QPushButton("1")
        self.but2 = QPushButton("2")
        self.but3 = QPushButton("3")
        self.but_plus = QPushButton("+")

        self.but1.setStyleSheet("background-color: green; color: white")
        self.but2.setStyleSheet("background-color: green; color: white")
        self.but3.setStyleSheet("background-color: green; color: white")
        self.but_plus.setStyleSheet("background-color: bleak; color: white")

        self.tortinchi_qator.addWidget(self.but3)
        self.tortinchi_qator.addWidget(self.but2)
        self.tortinchi_qator.addWidget(self.but1)
        self.tortinchi_qator.addWidget(self.but_plus)

        self.teng = QPushButton("=")
        self.oraqaga = QPushButton("<--")
        self.nuqta = QPushButton(".")
        self.but10 = QPushButton("0")

        self.nuqta.setStyleSheet("background-color: green; color: white")
        self.oraqaga.setStyleSheet("background-color: orange; color: white")
        self.but10.setStyleSheet("background-color: green; color: white")
        self.teng.setStyleSheet("background-color: bleak; color: white")

        self.beshinchi_qator.addWidget(self.oraqaga)
        self.beshinchi_qator.addWidget(self.but10)
        self.beshinchi_qator.addWidget(self.nuqta)
        self.beshinchi_qator.addWidget(self.teng)

        self.v_box.addLayout(self.first)
        self.v_box.addLayout(self.birinchi_qator)
        self.v_box.addLayout(self.ikkinchi_qator)
        self.v_box.addLayout(self.uchinchi_qator)
        self.v_box.addLayout(self.tortinchi_qator)
        self.v_box.addLayout(self.beshinchi_qator)

        self.but1.clicked.connect(self.press)
        self.but2.clicked.connect(self.press)
        self.but3.clicked.connect(self.press)
        self.but4.clicked.connect(self.press)
        self.but5.clicked.connect(self.press)
        self.but6.clicked.connect(self.press)
        self.but7.clicked.connect(self.press)
        self.but8.clicked.connect(self.press)
        self.but9.clicked.connect(self.press)
        self.but10.clicked.connect(self.press)
        self.clear.clicked.connect(self.tozala)
        self.teng.clicked.connect(self.hisobla)
        self.but_bol.clicked.connect(self.press)
        self.but_kop.clicked.connect(self.press)
        self.but_plus.clicked.connect(self.press)
        self.but_minus.clicked.connect(self.press)
        self.oraqaga.clicked.connect(self.orqaga_qayt)
        self.qavs1.clicked.connect(self.press)
        self.qavs2.clicked.connect(self.press)

        self.setLayout(self.v_box)
        self.show()

    def press(self):
        btn = self.sender()
        self.matn += btn.text()
        self.edit.setText(self.matn)
    print("Hammasi joyida")
    def tozala(self):
        self.matn = ""
        self.edit.setText(self.matn)

    def orqaga_qayt(self):
        self.matn = self.matn[:-1]
        self.edit.setText(self.matn)

    def hisobla(self):
        try:
            self.matn = str(eval(self.matn))
            self.edit.setText(self.matn)
        except:
            self.edit.setText(" 0 ga bolish mumkin emas")
            self.matn


res = QApplication([])
arr = Kanculyator()
res.exec_()