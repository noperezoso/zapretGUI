# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filters.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_FiltersWindow(object):
    def setupUi(self, FiltersWindow):
        if not FiltersWindow.objectName():
            FiltersWindow.setObjectName(u"FiltersWindow")
        FiltersWindow.setEnabled(True)
        FiltersWindow.resize(360, 430)
        FiltersWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.textEdit = QTextEdit(FiltersWindow)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 55, 320, 320))
        self.textEdit.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.comboBox = QComboBox(FiltersWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 320, 20))
        self.comboBox.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_3 = QPushButton(FiltersWindow)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 390, 80, 20))
        self.pushButton_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.pushButton_4 = QPushButton(FiltersWindow)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(260, 390, 80, 20))
        self.pushButton_4.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.retranslateUi(FiltersWindow)

        QMetaObject.connectSlotsByName(FiltersWindow)
    # setupUi

    def retranslateUi(self, FiltersWindow):
        FiltersWindow.setWindowTitle(QCoreApplication.translate("FiltersWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432", None))
        self.pushButton_3.setText(QCoreApplication.translate("FiltersWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("FiltersWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

