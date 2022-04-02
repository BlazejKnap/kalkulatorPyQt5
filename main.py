import sys
import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt5 import QtCore


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Kalkulator'
        self.left = 100
        self.top = 100
        self.width = 305
        self.height = 380
        self.liczba1 = 0
        self.wynik = 0
        self.znak = '+'
        self.pierwszy = True
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.operationLabel = QLabel(self)
        self.operationLabel.setFont(QFont('Arial', 15))
        self.operationLabel.setStyleSheet("border: 1px solid black;")
        self.operationLabel.setText("")
        self.operationLabel.move(5, 5)
        self.operationLabel.resize(295, 30)

        self.resultLabel = QLabel(self)
        self.resultLabel.setFont(QFont('Arial', 30))
        self.resultLabel.setStyleSheet("border: 1px solid black;")
        self.resultLabel.setAlignment(QtCore.Qt.AlignRight)
        self.resultLabel.setText("0")
        self.resultLabel.move(5, 30)
        self.resultLabel.resize(295, 70)

        self.button1 = QPushButton('1', self)
        self.button1.move(5, 270)
        self.button1.resize(70, 50)
        self.button1.setFont(QFont('Arial', 20))
        self.button1.clicked.connect(self.on_click1)

        self.button2 = QPushButton('2', self)
        self.button2.move(80, 270)
        self.button2.resize(70, 50)
        self.button2.setFont(QFont('Arial', 20))
        self.button2.clicked.connect(self.on_click2)

        self.button3 = QPushButton('3', self)
        self.button3.move(155, 270)
        self.button3.resize(70, 50)
        self.button3.setFont(QFont('Arial', 20))
        self.button3.clicked.connect(self.on_click3)

        self.button4 = QPushButton('4', self)
        self.button4.move(5, 215)
        self.button4.resize(70, 50)
        self.button4.setFont(QFont('Arial', 20))
        self.button4.clicked.connect(self.on_click4)

        self.button5 = QPushButton('5', self)
        self.button5.move(80, 215)
        self.button5.resize(70, 50)
        self.button5.setFont(QFont('Arial', 20))
        self.button5.clicked.connect(self.on_click5)

        self.button6 = QPushButton('6', self)
        self.button6.move(155, 215)
        self.button6.resize(70, 50)
        self.button6.setFont(QFont('Arial', 20))
        self.button6.clicked.connect(self.on_click6)

        self.button7 = QPushButton('7', self)
        self.button7.move(5, 160)
        self.button7.resize(70, 50)
        self.button7.setFont(QFont('Arial', 20))
        self.button7.clicked.connect(self.on_click7)

        self.button8 = QPushButton('8', self)
        self.button8.move(80, 160)
        self.button8.resize(70, 50)
        self.button8.setFont(QFont('Arial', 20))
        self.button8.clicked.connect(self.on_click8)

        self.button9 = QPushButton('9', self)
        self.button9.move(155, 160)
        self.button9.resize(70, 50)
        self.button9.setFont(QFont('Arial', 20))
        self.button9.clicked.connect(self.on_click9)

        self.button0 = QPushButton('0', self)
        self.button0.move(5, 325)
        self.button0.resize(70, 50)
        self.button0.setFont(QFont('Arial', 20))
        self.button0.clicked.connect(self.on_click0)

        self.buttonPlus = QPushButton('+', self)
        self.buttonPlus.move(230, 325)
        self.buttonPlus.resize(70, 50)
        self.buttonPlus.setFont(QFont('Arial', 20))
        self.buttonPlus.clicked.connect(self.on_clickPlus)

        self.buttonMinus = QPushButton('-', self)
        self.buttonMinus.move(230, 270)
        self.buttonMinus.resize(70, 50)
        self.buttonMinus.setFont(QFont('Arial', 20))
        self.buttonMinus.clicked.connect(self.on_clickMinus)

        self.buttonMultiplication = QPushButton('*', self)
        self.buttonMultiplication.move(230, 215)
        self.buttonMultiplication.resize(70, 50)
        self.buttonMultiplication.setFont(QFont('Arial', 20))
        self.buttonMultiplication.clicked.connect(self.on_clickMultiplication)

        self.buttonDivide = QPushButton('/', self)
        self.buttonDivide.move(230, 160)
        self.buttonDivide.resize(70, 50)
        self.buttonDivide.setFont(QFont('Arial', 20))
        self.buttonDivide.clicked.connect(self.on_clickDivide)


        self.buttonEqual = QPushButton('=', self)
        self.buttonEqual.move(80, 325)
        self.buttonEqual.resize(145, 50)
        self.buttonEqual.setFont(QFont('Arial', 20))
        self.buttonEqual.clicked.connect(self.on_clickEqual)
        self.buttonEqual.setEnabled(False)

        self.buttonChangeChar = QPushButton('+/-', self)
        self.buttonChangeChar.move(230, 105)
        self.buttonChangeChar.resize(70, 50)
        self.buttonChangeChar.setFont(QFont('Arial', 20))
        self.buttonChangeChar.clicked.connect(self.on_clickChangeChar)

        self.buttonSqrt = QPushButton('√', self)
        self.buttonSqrt.move(155, 105)
        self.buttonSqrt.resize(70, 50)
        self.buttonSqrt.setFont(QFont('Arial', 20))
        self.buttonSqrt.clicked.connect(self.on_clickSqrt)

        self.buttonPotega = QPushButton('^x', self)
        self.buttonPotega.move(80, 105)
        self.buttonPotega.resize(70, 50)
        self.buttonPotega.setFont(QFont('Arial', 20))
        self.buttonPotega.clicked.connect(self.on_clickPotega)

        self.buttonC = QPushButton('C', self)
        self.buttonC.move(5, 105)
        self.buttonC.resize(70, 50)
        self.buttonC.setFont(QFont('Arial', 20))
        self.buttonC.clicked.connect(self.on_clickC)

        self.show()


    def dzialanie(self):
        self.liczba1 = int(self.resultLabel.text())
        if self.znak == '+':
            self.wynik += self.liczba1
        elif self.znak == '*':
            self.wynik *= self.liczba1
        elif self.znak == '/':
            self.wynik /= self.liczba1
        elif self.znak == '-':
            self.wynik -= self.liczba1
        elif self.znak == '**':
            self.wynik = self.wynik ** self.liczba1

    def check(self):
        if self.pierwszy:
            self.operationLabel.setText(self.operationLabel.text() + str(int(self.liczba1)) + self.znak)
            self.resultLabel.setText("0")
            self.buttonEqual.setEnabled(True)
        else:
            self.operationLabel.setText(str(int(self.wynik)) + self.znak)
            self.resultLabel.setText("0")
            self.pierwszy = True
            self.buttonEqual.setEnabled(True)

    @pyqtSlot()
    def on_click1(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("1")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "1")

    @pyqtSlot()
    def on_click2(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("2")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "2")

    @pyqtSlot()
    def on_click3(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("3")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "3")

    @pyqtSlot()
    def on_click4(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("4")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "4")

    @pyqtSlot()
    def on_click5(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("5")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "5")

    @pyqtSlot()
    def on_click6(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("6")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "6")

    @pyqtSlot()
    def on_click7(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("7")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "7")

    @pyqtSlot()
    def on_click8(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("8")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "8")

    @pyqtSlot()
    def on_click9(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("9")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "9")

    @pyqtSlot()
    def on_click0(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("0")
        else:
            self.resultLabel.setText(self.resultLabel.text() + "0")

    @pyqtSlot()
    def on_clickPlus(self):
        self.dzialanie()
        self.znak = '+'
        self.check()

    @pyqtSlot()
    def on_clickMinus(self):
        self.dzialanie()
        self.znak = '-'
        self.check()

    @pyqtSlot()
    def on_clickMultiplication(self):
        self.dzialanie()
        self.znak = '*'
        self.check()

    @pyqtSlot()
    def on_clickDivide(self):
        self.dzialanie()
        self.znak = '/'
        self.check()

    @pyqtSlot()
    def on_clickEqual(self):
        self.dzialanie()
        self.buttonEqual.setEnabled(False)
        self.pierwszy = False
        self.operationLabel.setText(self.operationLabel.text() + str(int(self.liczba1)) + "=")
        self.resultLabel.setText(str(int(self.wynik)))
        self.liczba1 = self.wynik
        self.wynik = 0
        self.znak = '+'

    @pyqtSlot()
    def on_clickSqrt(self):
        self.liczba1 = int(self.resultLabel.text())
        self.buttonEqual.setEnabled(False)
        self.pierwszy = False
        self.operationLabel.setText("sqrt(" + str(self.liczba1) + ")=")
        self.wynik = math.sqrt(self.liczba1)
        self.resultLabel.setText(str(int(self.wynik)))
        self.liczba1 = self.wynik
        self.wynik = 0
        self.znak = '+'

    @pyqtSlot()
    def on_clickPotega(self):
        self.dzialanie()
        self.znak = '**'
        self.check()

    @pyqtSlot()
    def on_clickChangeChar(self):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText("0")
        else:
            self.liczba1 = int(self.resultLabel.text())
            self.liczba1 = self.liczba1 - self.liczba1 - self.liczba1
            self.resultLabel.setText(str(self.liczba1))
            self.liczba1 = 0

    @pyqtSlot()
    def on_clickC(self):
        self.buttonEqual.setEnabled(False)
        self.liczba1 = 0
        self.wynik = 0
        self.pierwszy = True
        self.znak = '+'
        self.resultLabel.setText("0")
        self.operationLabel.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

"""
Wykonał:
Błażej Knap
"""
