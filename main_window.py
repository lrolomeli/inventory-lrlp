# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windownouubk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(814, 592)
        MainWindow.setMinimumSize(QSize(814, 592))
        MainWindow.setMaximumSize(QSize(814, 592))
        icon = QIcon()
        icon.addFile(u"images/ppg_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(160, 160, 160);\n"
"alternate-background-color: rgb(174, 182, 255);")
        MainWindow.setIconSize(QSize(50, 50))
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        self.actionLoadBackupFile = QAction(MainWindow)
        self.actionLoadBackupFile.setObjectName(u"actionLoadBackupFile")
        self.actionGenBackupFile = QAction(MainWindow)
        self.actionGenBackupFile.setObjectName(u"actionGenBackupFile")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.product_filter_cb = QComboBox(self.centralwidget)
        self.product_filter_cb.setObjectName(u"product_filter_cb")
        self.product_filter_cb.setGeometry(QRect(400, 50, 161, 22))
        self.product_label = QLabel(self.centralwidget)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setGeometry(QRect(320, 50, 71, 20))
        self.product_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 275, 81))
        self.operations_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.operations_layout.setObjectName(u"operations_layout")
        self.operations_layout.setContentsMargins(0, 0, 0, 0)
        self.new_item_btn = QPushButton(self.horizontalLayoutWidget)
        self.new_item_btn.setObjectName(u"new_item_btn")
        icon1 = QIcon()
        icon1.addFile(u"images/new_item.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_item_btn.setIcon(icon1)
        self.new_item_btn.setIconSize(QSize(50, 50))
        self.new_item_btn.setAutoDefault(True)
        self.new_item_btn.setFlat(True)

        self.operations_layout.addWidget(self.new_item_btn)

        self.outcome_btn = QPushButton(self.horizontalLayoutWidget)
        self.outcome_btn.setObjectName(u"outcome_btn")
        icon2 = QIcon()
        icon2.addFile(u"images/sale.png", QSize(), QIcon.Normal, QIcon.Off)
        self.outcome_btn.setIcon(icon2)
        self.outcome_btn.setIconSize(QSize(50, 50))
        self.outcome_btn.setAutoDefault(True)
        self.outcome_btn.setFlat(True)

        self.operations_layout.addWidget(self.outcome_btn)

        self.income_btn = QPushButton(self.horizontalLayoutWidget)
        self.income_btn.setObjectName(u"income_btn")
        icon3 = QIcon()
        icon3.addFile(u"images/updating.png", QSize(), QIcon.Normal, QIcon.Off)
        self.income_btn.setIcon(icon3)
        self.income_btn.setIconSize(QSize(50, 50))
        self.income_btn.setAutoDefault(True)
        self.income_btn.setFlat(True)

        self.operations_layout.addWidget(self.income_btn)

        self.game_btn = QPushButton(self.horizontalLayoutWidget)
        self.game_btn.setObjectName(u"game_btn")
        icon4 = QIcon()
        icon4.addFile(u"images/game.png", QSize(), QIcon.Normal, QIcon.Off)
        self.game_btn.setIcon(icon4)
        self.game_btn.setIconSize(QSize(50, 50))
        self.game_btn.setAutoDefault(True)
        self.game_btn.setFlat(True)

        self.operations_layout.addWidget(self.game_btn)

        self.category_label = QLabel(self.centralwidget)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(320, 10, 81, 20))
        self.category_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.category_filter_cb = QComboBox(self.centralwidget)
        self.category_filter_cb.setObjectName(u"category_filter_cb")
        self.category_filter_cb.setGeometry(QRect(400, 10, 161, 22))
        self.product_searchbox = QLineEdit(self.centralwidget)
        self.product_searchbox.setObjectName(u"product_searchbox")
        self.product_searchbox.setGeometry(QRect(622, 20, 151, 41))
        self.product_searchbox.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.inventory_table = QTableWidget(self.centralwidget)
        if (self.inventory_table.columnCount() < 6):
            self.inventory_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.inventory_table.setObjectName(u"inventory_table")
        self.inventory_table.setGeometry(QRect(20, 130, 761, 381))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 814, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoadBackupFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGenBackupFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plasticos Plasa Inventario", None))
        self.actionLoadBackupFile.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo de Inventario...", None))
        self.actionGenBackupFile.setText(QCoreApplication.translate("MainWindow", u"Generar Respaldo de Inventario...", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.product_label.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.new_item_btn.setText("")
        self.outcome_btn.setText("")
        self.income_btn.setText("")
        self.game_btn.setText("")
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.product_searchbox.setText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        ___qtablewidgetitem = self.inventory_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.inventory_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CATEGORIA", None));
        ___qtablewidgetitem2 = self.inventory_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"COLOR", None));
        ___qtablewidgetitem3 = self.inventory_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        ___qtablewidgetitem4 = self.inventory_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COSTO", None));
        ___qtablewidgetitem5 = self.inventory_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"UBICACION", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

