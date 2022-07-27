import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.my_input = []
        # self.operand_1 = []
        # self.operand_2 = []

    def initUI(self):
        self.setGeometry(800, 400, 400, 700)
        self.setWindowTitle('Вычислительная машина')

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(400, 100)
        self.label.move(0, 0)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(100, 100)
        self.num_1.move(0, 300)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(100, 100)
        self.num_2.move(100, 300)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(100, 100)
        self.num_3.move(200, 300)

        self.div = QPushButton('/', self)
        self.div.resize(100, 100)
        self.div.move(300, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(100, 100)
        self.num_4.move(0, 200)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(100, 100)
        self.num_5.move(100, 200)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(100, 100)
        self.num_6.move(200, 200)

        self.mul = QPushButton('*', self)
        self.mul.resize(100, 100)
        self.mul.move(300, 200)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(100, 100)
        self.num_7.move(0, 100)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(100, 100)
        self.num_8.move(100, 100)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(100, 100)
        self.num_9.move(200, 100)

        self.plus = QPushButton('+', self)
        self.plus.resize(100, 100)
        self.plus.move(300, 300)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(100, 100)
        self.num_0.move(0, 400)

        self.minus = QPushButton('-', self)
        self.minus.resize(100, 100)
        self.minus.move(100, 400)

        self.step = QPushButton('^', self)
        self.step.resize(100, 100)
        self.step.move(200, 400)

        self.koren = QPushButton('√', self)
        self.koren.resize(100, 100)
        self.koren.move(300, 400)

        self.ravno = QPushButton('=', self)
        self.ravno.resize(300, 100)
        self.ravno.move(0, 600)

        self.clean = QPushButton('c', self)
        self.clean.resize(100, 100)
        self.clean.move(300, 600)

        self.proc = QPushButton('%', self)
        self.proc.resize(150, 100)
        self.proc.move(0, 500)

        self.delc = QPushButton('//', self)
        self.delc.resize(100, 100)
        self.delc.move(300, 500)

        self.kvadr = QPushButton('²', self)
        self.kvadr.resize(150, 100)
        self.kvadr.move(150, 500)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.tree)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minys_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.koren.clicked.connect(self.sqrt_1)
        self.ravno.clicked.connect(self.ravno_1)
        self.clean.clicked.connect(self.clean_1)
        self.proc.clicked.connect(self.proc_1)
        self.kvadr.clicked.connect(self.kvadr_1)
        self.delc.clicked.connect(self.delc_1)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def tree(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minys_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def proc_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def delc_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def kvadr_1(self):
        self.operation = '²'
        self.operand_1 = float(self.label.text())


    def clean_1(self):
        self.operation = 'c'
        self.label.setText('')

    def ravno_1(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezylt = self.operand_1+self.operand_2
        if self.operation == '-':
            self.rezylt = self.operand_1 - self.operand_2
        if self.operation == '*':
            self.rezylt = self.operand_1 * self.operand_2
        if self.operation == '/':
            if self.operand_2 == 0:
                self.rezylt = 'error'
            else:
                self.rezylt = self.operand_1 / self.operand_2
        if self.operation == '^':
            self.rezylt = self.operand_1 ** self.operand_2
        if self.operation == '√':
            self.rezylt = self.operand_1 ** (1/self.operand_2)
        if self.operation == '%':
            self.rezylt = self.operand_1/100 * self.operand_2
        if self.operation == '//':
            self.rezylt = self.operand_1 // self.operand_2
        if self.operation == '²':
            self.rezylt = self.operand_1 ** 2
        self.label.setText(str(self.rezylt))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lp = Calculator()
    lp.show()
    sys.exit(app.exec())
