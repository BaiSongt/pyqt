# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans_unit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 309)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 371, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(500, 40))

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 30))
        font1 = QFont()
        font1.setPointSize(25)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(500, 40))

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(500, 40))
        font2 = QFont()
        font2.setPointSize(15)
        self.comboBox_3.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_3, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

