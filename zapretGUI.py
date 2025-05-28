# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zapretGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(280, 260)
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_1 = QGroupBox(self.centralwidget)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(20, 80, 240, 150))
        self.groupBox_1.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.groupBox_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_13 = QPushButton(self.groupBox_1)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(145, 25, 80, 20))
        self.pushButton_13.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_14 = QPushButton(self.groupBox_1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(145, 55, 80, 20))
        self.pushButton_14.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_11 = QPushButton(self.groupBox_1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setGeometry(QRect(145, 85, 80, 20))
        self.pushButton_11.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_12 = QPushButton(self.groupBox_1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setGeometry(QRect(145, 115, 80, 20))
        self.pushButton_12.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.radioButton_11 = QRadioButton(self.groupBox_1)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(15, 55, 80, 20))
        self.radioButton_11.setChecked(True)
        self.radioButton_12 = QRadioButton(self.groupBox_1)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(15, 85, 80, 20))
        self.radioButton_13 = QRadioButton(self.groupBox_1)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setGeometry(QRect(15, 115, 80, 20))
        self.label_11 = QLabel(self.groupBox_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(15, 25, 80, 20))
        self.pushButton_02 = QPushButton(self.centralwidget)
        self.pushButton_02.setObjectName(u"pushButton_02")
        self.pushButton_02.setGeometry(QRect(165, 20, 80, 50))
        self.pushButton_02.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_00 = QPushButton(self.centralwidget)
        self.pushButton_00.setObjectName(u"pushButton_00")
        self.pushButton_00.setGeometry(QRect(35, 20, 80, 50))
        self.pushButton_00.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.radioButton_11.toggled.connect(self.pushButton_11.setDisabled)
        self.radioButton_11.toggled.connect(self.pushButton_12.setDisabled)
        self.radioButton_12.toggled.connect(self.pushButton_11.setEnabled)
        self.radioButton_13.toggled.connect(self.pushButton_11.setEnabled)
        self.radioButton_12.toggled.connect(self.pushButton_12.setEnabled)
        self.radioButton_13.toggled.connect(self.pushButton_12.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"zapretGUI", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u0430", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0437\u0430\u043f\u0443\u0441\u043a:", None))
        self.pushButton_02.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.pushButton_00.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

