# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product_dialogrUQkFL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_editProduct(object):
    def setupUi(self, editProduct):
        if not editProduct.objectName():
            editProduct.setObjectName(u"editProduct")
        editProduct.resize(684, 302)
        editProduct.setStyleSheet(u"background-color: rgb(160, 160, 160);")
        self.verticalLayoutWidget = QWidget(editProduct)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 160, 271))
        self.label_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.verticalLayoutWidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.name_label)

        self.quantity_label = QLabel(self.verticalLayoutWidget)
        self.quantity_label.setObjectName(u"quantity_label")
        self.quantity_label.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.label_layout.addWidget(self.quantity_label)

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

        self.verticalLayoutWidget_2 = QWidget(editProduct)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(179, 20, 251, 271))
        self.txtedit_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.txtedit_layout.setObjectName(u"txtedit_layout")
        self.txtedit_layout.setContentsMargins(0, 0, 0, 0)
        self.name_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.name_txtedit.setObjectName(u"name_txtedit")
        self.name_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.name_txtedit.setReadOnly(False)

        self.txtedit_layout.addWidget(self.name_txtedit)

        self.quantity_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.quantity_txtedit.setObjectName(u"quantity_txtedit")
        self.quantity_txtedit.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.quantity_txtedit.setReadOnly(True)

        self.txtedit_layout.addWidget(self.quantity_txtedit)

        self.category_txtedit = QLineEdit(self.verticalLayoutWidget_2)
        self.category_txtedit.setObjectName(u"category_txtedit")
        self.category_txtedit.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.category_txtedit.setReadOnly(True)

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
        self.color_txtedit.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.color_txtedit.setReadOnly(True)

        self.txtedit_layout.addWidget(self.color_txtedit)

        self.verticalLayoutWidget_3 = QWidget(editProduct)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(440, 50, 232, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.update_product_btn = QPushButton(self.verticalLayoutWidget_3)
        self.update_product_btn.setObjectName(u"update_product_btn")
        icon = QIcon()
        icon.addFile(u"images/updates.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_product_btn.setIcon(icon)
        self.update_product_btn.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.update_product_btn)

        self.erase_btn = QPushButton(self.verticalLayoutWidget_3)
        self.erase_btn.setObjectName(u"erase_btn")
        icon1 = QIcon()
        icon1.addFile(u"images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.erase_btn.setIcon(icon1)
        self.erase_btn.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.erase_btn)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget_3)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(editProduct)

        QMetaObject.connectSlotsByName(editProduct)
    # setupUi

    def retranslateUi(self, editProduct):
        editProduct.setWindowTitle(QCoreApplication.translate("editProduct", u"A\u00f1adir Nuevo Producto", None))
        self.name_label.setText(QCoreApplication.translate("editProduct", u"Nombre", None))
        self.quantity_label.setText(QCoreApplication.translate("editProduct", u"Cantidad", None))
        self.category_label.setText(QCoreApplication.translate("editProduct", u"Categoria", None))
        self.cost_label.setText(QCoreApplication.translate("editProduct", u"Costo", None))
        self.location_label.setText(QCoreApplication.translate("editProduct", u"Ubicacion", None))
        self.color_label.setText(QCoreApplication.translate("editProduct", u"Color", None))
        self.category_txtedit.setText("")
        self.cost_txtedit.setText("")
        self.location_txtedit.setText("")
        self.color_txtedit.setText("")
        self.update_product_btn.setText(QCoreApplication.translate("editProduct", u"ACTUALIZAR", None))
        self.erase_btn.setText(QCoreApplication.translate("editProduct", u"BORRAR PRODUCTO", None))
    # retranslateUi

