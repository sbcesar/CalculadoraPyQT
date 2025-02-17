# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(300, 400))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #282828;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 301, 61))
        self.label.setStyleSheet(u"QWidget {\n"
"	padding-right: 20px;\n"
"	padding-top: 15px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	background-color: #282828;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 60, 300, 321))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"}")
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 281, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_raiz = QPushButton(self.gridLayoutWidget)
        self.pushButton_raiz.setObjectName(u"pushButton_raiz")
        sizePolicy.setHeightForWidth(self.pushButton_raiz.sizePolicy().hasHeightForWidth())
        self.pushButton_raiz.setSizePolicy(sizePolicy)
        self.pushButton_raiz.setMinimumSize(QSize(40, 40))
        self.pushButton_raiz.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_raiz, 1, 2, 1, 1)

        self.pushButton_clear = QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setMinimumSize(QSize(40, 40))
        self.pushButton_clear.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_clear, 0, 2, 1, 1)

        self.pushButton_par_izq = QPushButton(self.gridLayoutWidget)
        self.pushButton_par_izq.setObjectName(u"pushButton_par_izq")
        sizePolicy.setHeightForWidth(self.pushButton_par_izq.sizePolicy().hasHeightForWidth())
        self.pushButton_par_izq.setSizePolicy(sizePolicy)
        self.pushButton_par_izq.setMinimumSize(QSize(40, 40))
        self.pushButton_par_izq.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_par_izq, 1, 0, 1, 1)

        self.pushButton_del = QPushButton(self.gridLayoutWidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        sizePolicy.setHeightForWidth(self.pushButton_del.sizePolicy().hasHeightForWidth())
        self.pushButton_del.setSizePolicy(sizePolicy)
        self.pushButton_del.setMinimumSize(QSize(40, 40))
        self.pushButton_del.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_del, 0, 3, 1, 1)

        self.pushButton_ce = QPushButton(self.gridLayoutWidget)
        self.pushButton_ce.setObjectName(u"pushButton_ce")
        sizePolicy.setHeightForWidth(self.pushButton_ce.sizePolicy().hasHeightForWidth())
        self.pushButton_ce.setSizePolicy(sizePolicy)
        self.pushButton_ce.setMinimumSize(QSize(40, 40))
        self.pushButton_ce.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_ce, 0, 1, 1, 1)

        self.pushButton_par_der = QPushButton(self.gridLayoutWidget)
        self.pushButton_par_der.setObjectName(u"pushButton_par_der")
        sizePolicy.setHeightForWidth(self.pushButton_par_der.sizePolicy().hasHeightForWidth())
        self.pushButton_par_der.setSizePolicy(sizePolicy)
        self.pushButton_par_der.setMinimumSize(QSize(40, 40))
        self.pushButton_par_der.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_par_der, 1, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QSize(40, 40))
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_div = QPushButton(self.gridLayoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        self.pushButton_div.setMinimumSize(QSize(40, 40))
        self.pushButton_div.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_porc = QPushButton(self.gridLayoutWidget)
        self.pushButton_porc.setObjectName(u"pushButton_porc")
        sizePolicy.setHeightForWidth(self.pushButton_porc.sizePolicy().hasHeightForWidth())
        self.pushButton_porc.setSizePolicy(sizePolicy)
        self.pushButton_porc.setMinimumSize(QSize(40, 40))
        self.pushButton_porc.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_porc, 0, 0, 1, 1)

        self.pushButton_hist = QPushButton(self.gridLayoutWidget)
        self.pushButton_hist.setObjectName(u"pushButton_hist")
        sizePolicy.setHeightForWidth(self.pushButton_hist.sizePolicy().hasHeightForWidth())
        self.pushButton_hist.setSizePolicy(sizePolicy)
        self.pushButton_hist.setMinimumSize(QSize(40, 40))
        self.pushButton_hist.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_hist, 5, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_mul = QPushButton(self.gridLayoutWidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        self.pushButton_mul.setMinimumSize(QSize(40, 40))
        self.pushButton_mul.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_res = QPushButton(self.gridLayoutWidget)
        self.pushButton_res.setObjectName(u"pushButton_res")
        sizePolicy.setHeightForWidth(self.pushButton_res.sizePolicy().hasHeightForWidth())
        self.pushButton_res.setSizePolicy(sizePolicy)
        self.pushButton_res.setMinimumSize(QSize(40, 40))
        self.pushButton_res.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_res, 3, 3, 1, 1)

        self.pushButton_sum = QPushButton(self.gridLayoutWidget)
        self.pushButton_sum.setObjectName(u"pushButton_sum")
        sizePolicy.setHeightForWidth(self.pushButton_sum.sizePolicy().hasHeightForWidth())
        self.pushButton_sum.setSizePolicy(sizePolicy)
        self.pushButton_sum.setMinimumSize(QSize(40, 40))
        self.pushButton_sum.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_sum, 4, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QSize(40, 40))
        self.pushButton_0.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)

        self.pushButton_punto = QPushButton(self.gridLayoutWidget)
        self.pushButton_punto.setObjectName(u"pushButton_punto")
        sizePolicy.setHeightForWidth(self.pushButton_punto.sizePolicy().hasHeightForWidth())
        self.pushButton_punto.setSizePolicy(sizePolicy)
        self.pushButton_punto.setMinimumSize(QSize(40, 40))
        self.pushButton_punto.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_punto, 5, 2, 1, 1)

        self.pushButton_igual = QPushButton(self.gridLayoutWidget)
        self.pushButton_igual.setObjectName(u"pushButton_igual")
        sizePolicy.setHeightForWidth(self.pushButton_igual.sizePolicy().hasHeightForWidth())
        self.pushButton_igual.setSizePolicy(sizePolicy)
        self.pushButton_igual.setMinimumSize(QSize(40, 40))
        self.pushButton_igual.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #bf0000;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_hist,\n"
"QPushButton#pushButton_igual {\n"
"	background-color: #bf0000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_igual, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_par_izq.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.pushButton_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_par_der.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_porc.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_hist.setText(QCoreApplication.translate("MainWindow", u"\u2261", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_mul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_res.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_punto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

