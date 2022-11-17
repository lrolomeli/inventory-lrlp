# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_product_dialogrAyXgy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewProduct(object):
    def setupUi(self, NewProduct):
        if not NewProduct.objectName():
            NewProduct.setObjectName(u"NewProduct")
        NewProduct.resize(643, 302)
        NewProduct.setStyleSheet(u"background-color: rgb(160, 160, 160);")
        self.add_product_btn = QPushButton(NewProduct)
        self.add_product_btn.setObjectName(u"add_product_btn")
        self.add_product_btn.setGeometry(QRect(480, 110, 121, 71))
        icon = QIcon()
        icon.addFile(u"images/add_product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_product_btn.setIcon(icon)
        self.verticalLayoutWidget = QWidget(NewProduct)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 160, 271))
        self.label_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.verticalLayoutWidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.name_label)

        self.qty_label = QLabel(self.verticalLayoutWidget)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.qty_label)

        self.category_label = QLabel(self.verticalLayoutWidget)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.category_label)

        self.cost_label = QLabel(self.verticalLayoutWidget)
        self.cost_label.setObjectName(u"cost_label")
        self.cost_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.cost_label)

        self.location_label = QLabel(self.verticalLayoutWidget)
        self.location_label.setObjectName(u"location_label")
        self.location_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.location_label)

        self.color_label = QLabel(self.verticalLayoutWidget)
        self.color_label.setObjectName(u"color_label")
        self.color_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.color_label)

        self.verticalLayoutWidget_2 = QWidget(NewProduct)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(179, 20, 251, 271))
        self.txtedit_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.txtedit_layout.setObjectName(u"txtedit_layout")
        self.txtedit_layout.setContentsMargins(0, 0, 0, 0)
        self.name_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.name_txtedit.setObjectName(u"name_txtedit")
        self.name_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.name_txtedit)

        self.qty_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.qty_txtedit.setObjectName(u"qty_txtedit")
        self.qty_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.qty_txtedit)

        self.category_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.category_txtedit.setObjectName(u"category_txtedit")
        self.category_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.category_txtedit)

        self.cost_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.cost_txtedit.setObjectName(u"cost_txtedit")
        self.cost_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.cost_txtedit)

        self.location_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.location_txtedit.setObjectName(u"location_txtedit")
        self.location_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.location_txtedit)

        self.color_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.color_txtedit.setObjectName(u"color_txtedit")
        self.color_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.txtedit_layout.addWidget(self.color_txtedit)


        self.retranslateUi(NewProduct)

        QMetaObject.connectSlotsByName(NewProduct)
    # setupUi

    def retranslateUi(self, NewProduct):
        NewProduct.setWindowTitle(QCoreApplication.translate("NewProduct", u"A\u00f1adir Nuevo Producto", None))
        self.add_product_btn.setText(QCoreApplication.translate("NewProduct", u"Agregar", None))
        self.name_label.setText(QCoreApplication.translate("NewProduct", u"Nombre", None))
        self.qty_label.setText(QCoreApplication.translate("NewProduct", u"Cantidad", None))
        self.category_label.setText(QCoreApplication.translate("NewProduct", u"Categoria", None))
        self.cost_label.setText(QCoreApplication.translate("NewProduct", u"Costo", None))
        self.location_label.setText(QCoreApplication.translate("NewProduct", u"Ubicacion", None))
        self.color_label.setText(QCoreApplication.translate("NewProduct", u"Color", None))
        self.category_txtedit.setText("")
        self.cost_txtedit.setText("")
        self.location_txtedit.setText("")
        self.color_txtedit.setText("")
    # retranslateUi

