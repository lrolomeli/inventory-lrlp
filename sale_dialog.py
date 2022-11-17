# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sale_dialogCWjPbb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sale_dialog(object):
    def setupUi(self, sale_dialog):
        if not sale_dialog.objectName():
            sale_dialog.setObjectName(u"sale_dialog")
        sale_dialog.resize(500, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sale_dialog.sizePolicy().hasHeightForWidth())
        sale_dialog.setSizePolicy(sizePolicy)
        sale_dialog.setMinimumSize(QSize(500, 200))
        sale_dialog.setMaximumSize(QSize(500, 200))
        sale_dialog.setStyleSheet(u"background-color: rgb(160, 160, 160);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cancel_btn = QDialogButtonBox(sale_dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(190, 160, 101, 32))
        self.cancel_btn.setOrientation(Qt.Horizontal)
        self.cancel_btn.setStandardButtons(QDialogButtonBox.Cancel)
        self.formLayoutWidget = QWidget(sale_dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 30, 251, 101))
        self.product_form_layout = QFormLayout(self.formLayoutWidget)
        self.product_form_layout.setObjectName(u"product_form_layout")
        self.product_form_layout.setContentsMargins(0, 0, 0, 0)
        self.product_label = QLabel(self.formLayoutWidget)
        self.product_label.setObjectName(u"product_label")

        self.product_form_layout.setWidget(0, QFormLayout.LabelRole, self.product_label)

        self.product_txtedit = QLineEdit(self.formLayoutWidget)
        self.product_txtedit.setObjectName(u"product_txtedit")
        self.product_txtedit.setMinimumSize(QSize(0, 0))
        self.product_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.product_form_layout.setWidget(0, QFormLayout.FieldRole, self.product_txtedit)

        self.qty_txtedit = QLineEdit(self.formLayoutWidget)
        self.qty_txtedit.setObjectName(u"qty_txtedit")
        self.qty_txtedit.setMinimumSize(QSize(0, 0))
        self.qty_txtedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.product_form_layout.setWidget(1, QFormLayout.FieldRole, self.qty_txtedit)

        self.location_label = QLabel(self.formLayoutWidget)
        self.location_label.setObjectName(u"location_label")

        self.product_form_layout.setWidget(2, QFormLayout.LabelRole, self.location_label)

        self.location_filter_cb = QComboBox(self.formLayoutWidget)
        self.location_filter_cb.setObjectName(u"location_filter_cb")

        self.product_form_layout.setWidget(2, QFormLayout.FieldRole, self.location_filter_cb)

        self.qty_label = QLabel(self.formLayoutWidget)
        self.qty_label.setObjectName(u"qty_label")

        self.product_form_layout.setWidget(1, QFormLayout.LabelRole, self.qty_label)

        self.verticalLayoutWidget = QWidget(sale_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(310, 30, 160, 106))
        self.cart_buttons = QVBoxLayout(self.verticalLayoutWidget)
        self.cart_buttons.setObjectName(u"cart_buttons")
        self.cart_buttons.setContentsMargins(0, 0, 0, 0)
        self.addBasket_btn = QPushButton(self.verticalLayoutWidget)
        self.addBasket_btn.setObjectName(u"addBasket_btn")
        icon = QIcon()
        icon.addFile(u"images/add2cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addBasket_btn.setIcon(icon)

        self.cart_buttons.addWidget(self.addBasket_btn)

        self.watchBasket_btn = QPushButton(self.verticalLayoutWidget)
        self.watchBasket_btn.setObjectName(u"watchBasket_btn")
        icon1 = QIcon()
        icon1.addFile(u"images/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.watchBasket_btn.setIcon(icon1)

        self.cart_buttons.addWidget(self.watchBasket_btn)

        self.sale_btn = QPushButton(self.verticalLayoutWidget)
        self.sale_btn.setObjectName(u"sale_btn")

        self.cart_buttons.addWidget(self.sale_btn)


        self.retranslateUi(sale_dialog)
        self.cancel_btn.accepted.connect(sale_dialog.accept)
        self.cancel_btn.rejected.connect(sale_dialog.reject)

        QMetaObject.connectSlotsByName(sale_dialog)
    # setupUi

    def retranslateUi(self, sale_dialog):
        sale_dialog.setWindowTitle(QCoreApplication.translate("sale_dialog", u"Salidas", None))
        self.product_label.setText(QCoreApplication.translate("sale_dialog", u"Producto", None))
        self.location_label.setText(QCoreApplication.translate("sale_dialog", u"Ubicacion", None))
        self.qty_label.setText(QCoreApplication.translate("sale_dialog", u"Cantidad", None))
        self.addBasket_btn.setText(QCoreApplication.translate("sale_dialog", u"A\u00f1adir al Carrito", None))
        self.watchBasket_btn.setText(QCoreApplication.translate("sale_dialog", u"Ver Carrito", None))
        self.sale_btn.setText(QCoreApplication.translate("sale_dialog", u"Confirmar Salida", None))
    # retranslateUi

