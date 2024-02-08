from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import *
from ui_calculator import Ui_MainWindow
from calculator_operations import Operations


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Parent Initializer
        super().__init__()
        self.setupUi(self)
        self.operations = Operations(self.result_value, self.expression_label)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowTitle("Calculator")
        self.click_event_trigger()
        self.offset = QPoint()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_C:
            self.operations.clear_display()
        elif event.key() == Qt.Key_Backspace:
            self.operations.delete_single_value()
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Equal:
            self.operations.set_calculated_values()
        elif event.key() < 128:  # sure that it is valid ascii code
            match chr(event.key()):
                case '9':
                    self.operations.update_display('9')
                case '8':
                    self.operations.update_display('8')
                case '7':
                    self.operations.update_display('7')
                case '6':
                    self.operations.update_display('6')
                case '5':
                    self.operations.update_display('5')
                case '4':
                    self.operations.update_display('4')
                case '3':
                    self.operations.update_display('3')
                case '2':
                    self.operations.update_display('2')
                case '1':
                    self.operations.update_display('1')
                case '0':
                    self.operations.update_display('0')
                case '+':
                    self.operations.update_display('+')
                case '-':
                    self.operations.update_display('-')
                case '*':
                    self.operations.update_display('x')
                case '/':
                    self.operations.update_display('÷')
                case '%':
                    self.operations.update_display('%')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            global_pos = event.globalPosition().toPoint() - self.offset
            self.move(global_pos)

    def mouseReleaseEvent(self, event):
        self.offset = QPoint()

    def click_event_trigger(self):
        self.zero_btn.clicked.connect(lambda: self.operations.update_display('0'))
        self.one_btn.clicked.connect(lambda: self.operations.update_display('1'))
        self.two_btn.clicked.connect(lambda: self.operations.update_display('2'))
        self.three_btn.clicked.connect(lambda: self.operations.update_display('3'))
        self.four_btn.clicked.connect(lambda: self.operations.update_display('4'))
        self.five_btn.clicked.connect(lambda: self.operations.update_display('5'))
        self.six_btn.clicked.connect(lambda: self.operations.update_display('6'))
        self.seven_btn.clicked.connect(lambda: self.operations.update_display('7'))
        self.eight_btn.clicked.connect(lambda: self.operations.update_display('8'))
        self.nine_btn.clicked.connect(lambda: self.operations.update_display('9'))
        self.add_btn.clicked.connect(lambda: self.operations.update_display('+'))
        self.sub_btn.clicked.connect(lambda: self.operations.update_display('-'))
        self.mul_btn.clicked.connect(lambda: self.operations.update_display('x'))
        self.divide_btn.clicked.connect(lambda: self.operations.update_display('÷'))
        self.modulus_btn.clicked.connect(lambda: self.operations.update_display('%'))
        self.cube_btn.clicked.connect(lambda: self.operations.update_display('x³'))
        self.square_btn.clicked.connect(lambda: self.operations.update_display('x²'))
        self.sign_btn.clicked.connect(lambda: self.operations.update_display('-'))

        self.sign_btn.clicked.connect(lambda: self.operations.update_display('-'))
        self.erase_btn.clicked.connect(self.operations.delete_single_value)
        self.c_btn.clicked.connect(self.operations.clear_display)
        self.equal_to_btn.clicked.connect(lambda: self.operations.set_calculated_values())
        self.close_btn.clicked.connect(self.close)


app = QApplication()
win = Window()
win.show()
app.exec()
