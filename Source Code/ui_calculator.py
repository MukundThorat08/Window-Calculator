# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorbCpNBX.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(340, 570))
        MainWindow.setStyleSheet(u"#menu_bar{\n"
"	background-color: transparent;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #0E1525;\n"
"}\n"
"#gridWidget *{\n"
"	background-color: #1C2334;\n"
"	color: #7488A7;\n"
"	border-radius: 5px;\n"
"	font: 16pt \"Product Sans\";\n"
"}\n"
"#gridWidget *:hover{\n"
"	background-color: #222B41;\n"
"}\n"
"#calculator_label{\n"
"	color: #7488A7;\n"
"	font: 25px \"Product Sans\";\n"
"}\n"
"#close_btn{\n"
"	background-color: #2C3448;\n"
"	border-radius: 5px;\n"
"}\n"
"#result_value{\n"
"	color: #7488A7;\n"
"	font: 30px \"Product Sans\";\n"
"}\n"
"#expression_label{\n"
"	color: #7488A7;\n"
"	font: 20px \"Product Sans\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_bar = QPushButton(self.header)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(30, 30))
        self.menu_bar.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/calculator_icon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.menu_bar.setIcon(icon)
        self.menu_bar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.menu_bar, 0, Qt.AlignLeft)

        self.calculator_label = QLabel(self.header)
        self.calculator_label.setObjectName(u"calculator_label")

        self.horizontalLayout.addWidget(self.calculator_label)

        self.close_btn = QPushButton(self.header)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setMaximumSize(QSize(9999, 9999))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/close.svg", QSize(), QIcon.Normal, QIcon.On)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.close_btn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 120))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.expression_label = QLabel(self.widget_2)
        self.expression_label.setObjectName(u"expression_label")

        self.verticalLayout_3.addWidget(self.expression_label, 0, Qt.AlignRight)

        self.result_value = QLabel(self.widget_2)
        self.result_value.setObjectName(u"result_value")

        self.verticalLayout_3.addWidget(self.result_value, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignRight)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridWidget = QWidget(self.widget_3)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.modulus_btn = QPushButton(self.gridWidget)
        self.modulus_btn.setObjectName(u"modulus_btn")
        self.modulus_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.modulus_btn, 1, 2, 1, 1)

        self.one_btn = QPushButton(self.gridWidget)
        self.one_btn.setObjectName(u"one_btn")
        self.one_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.one_btn, 4, 0, 1, 1)

        self.divide_btn = QPushButton(self.gridWidget)
        self.divide_btn.setObjectName(u"divide_btn")
        self.divide_btn.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.divide_btn, 1, 3, 1, 1)

        self.zero_btn = QPushButton(self.gridWidget)
        self.zero_btn.setObjectName(u"zero_btn")
        self.zero_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.zero_btn, 5, 1, 1, 1)

        self.eight_btn = QPushButton(self.gridWidget)
        self.eight_btn.setObjectName(u"eight_btn")
        self.eight_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.eight_btn, 2, 1, 1, 1)

        self.square_btn = QPushButton(self.gridWidget)
        self.square_btn.setObjectName(u"square_btn")
        self.square_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.square_btn, 1, 1, 1, 1)

        self.seven_btn = QPushButton(self.gridWidget)
        self.seven_btn.setObjectName(u"seven_btn")
        self.seven_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.seven_btn, 2, 0, 1, 1)

        self.cube_btn = QPushButton(self.gridWidget)
        self.cube_btn.setObjectName(u"cube_btn")
        self.cube_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.cube_btn, 1, 0, 1, 1)

        self.nine_btn = QPushButton(self.gridWidget)
        self.nine_btn.setObjectName(u"nine_btn")
        self.nine_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.nine_btn, 2, 2, 1, 1)

        self.equal_to_btn = QPushButton(self.gridWidget)
        self.equal_to_btn.setObjectName(u"equal_to_btn")
        self.equal_to_btn.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.equal_to_btn, 5, 3, 1, 1)

        self.erase_btn = QPushButton(self.gridWidget)
        self.erase_btn.setObjectName(u"erase_btn")
        self.erase_btn.setMinimumSize(QSize(100, 60))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/backspace.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.erase_btn.setIcon(icon2)
        self.erase_btn.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.erase_btn, 0, 3, 1, 1)

        self.two_btn = QPushButton(self.gridWidget)
        self.two_btn.setObjectName(u"two_btn")
        self.two_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.two_btn, 4, 1, 1, 1)

        self.sub_btn = QPushButton(self.gridWidget)
        self.sub_btn.setObjectName(u"sub_btn")
        self.sub_btn.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.sub_btn, 3, 3, 1, 1)

        self.add_btn = QPushButton(self.gridWidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.add_btn, 4, 3, 1, 1)

        self.six_btn = QPushButton(self.gridWidget)
        self.six_btn.setObjectName(u"six_btn")
        self.six_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.six_btn, 3, 2, 1, 1)

        self.dot_btn = QPushButton(self.gridWidget)
        self.dot_btn.setObjectName(u"dot_btn")
        self.dot_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.dot_btn, 5, 2, 1, 1)

        self.sign_btn = QPushButton(self.gridWidget)
        self.sign_btn.setObjectName(u"sign_btn")
        self.sign_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.sign_btn, 5, 0, 1, 1)

        self.three_btn = QPushButton(self.gridWidget)
        self.three_btn.setObjectName(u"three_btn")
        self.three_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.three_btn, 4, 2, 1, 1)

        self.mul_btn = QPushButton(self.gridWidget)
        self.mul_btn.setObjectName(u"mul_btn")
        self.mul_btn.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.mul_btn, 2, 3, 1, 1)

        self.four_btn = QPushButton(self.gridWidget)
        self.four_btn.setObjectName(u"four_btn")
        self.four_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.four_btn, 3, 0, 1, 1)

        self.five_btn = QPushButton(self.gridWidget)
        self.five_btn.setObjectName(u"five_btn")
        self.five_btn.setMinimumSize(QSize(70, 60))

        self.gridLayout.addWidget(self.five_btn, 3, 1, 1, 1)

        self.c_btn = QPushButton(self.gridWidget)
        self.c_btn.setObjectName(u"c_btn")
        self.c_btn.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.c_btn, 0, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.gridWidget)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_bar.setText("")
        self.calculator_label.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.close_btn.setText("")
        self.expression_label.setText("")
        self.result_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.modulus_btn.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.one_btn.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.divide_btn.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.zero_btn.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.eight_btn.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.square_btn.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.seven_btn.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.cube_btn.setText(QCoreApplication.translate("MainWindow", u"x\u00b3", None))
        self.nine_btn.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.equal_to_btn.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.erase_btn.setText("")
        self.two_btn.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.six_btn.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.dot_btn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.sign_btn.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.three_btn.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.mul_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.four_btn.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.five_btn.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.c_btn.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

