# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器_布局.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(422, 444)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 4, 0, 1, 1)

        self.pushButton_19 = QPushButton(Form)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 4, 1, 1, 1)

        self.pushButton_20 = QPushButton(Form)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout.addWidget(self.pushButton_20, 4, 2, 1, 1)

        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 5, 0, 1, 1)

        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 5, 1, 1, 1)

        self.pushButton_21 = QPushButton(Form)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout.addWidget(self.pushButton_21, 5, 2, 1, 1)

        self.pushButton_24 = QPushButton(Form)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout.addWidget(self.pushButton_24, 6, 0, 1, 1)

        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 6, 1, 1, 1)

        self.pushButton_23 = QPushButton(Form)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout.addWidget(self.pushButton_23, 6, 2, 1, 1)

        self.pushButton_22 = QPushButton(Form)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout.addWidget(self.pushButton_22, 7, 0, 1, 1)

        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 7, 1, 1, 1)

        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 7, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

