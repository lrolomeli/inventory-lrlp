# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_data_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_NewProduct(object):
    def setupUi(self, NewProduct):
        NewProduct.setObjectName("NewProduct")
        NewProduct.resize(443, 378)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProduct)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(NewProduct)
        self.label.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(NewProduct)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 120, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(NewProduct)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 160, 113, 22))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 200, 113, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(NewProduct)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 55, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 240, 113, 22))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(NewProduct)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(NewProduct)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 280, 113, 22))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(NewProduct)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 55, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(NewProduct)
        self.pushButton.setGeometry(QtCore.QRect(240, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(NewProduct)
        self.buttonBox.accepted.connect(NewProduct.accept)
        self.buttonBox.rejected.connect(NewProduct.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProduct)

    def retranslateUi(self, NewProduct):
        _translate = QtCore.QCoreApplication.translate
        NewProduct.setWindowTitle(_translate("NewProduct", "Añadir Nuevo Producto"))
        self.label.setText(_translate("NewProduct", "Nombre"))
        self.label_2.setText(_translate("NewProduct", "Cantidad"))
        self.label_3.setText(_translate("NewProduct", "Categoria"))
        self.label_4.setText(_translate("NewProduct", "Costo"))
        self.label_5.setText(_translate("NewProduct", "Ubicacion"))
        self.label_7.setText(_translate("NewProduct", "Color"))
        self.pushButton.setText(_translate("NewProduct", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewProduct = QtWidgets.QDialog()
    ui = Ui_NewProduct()
    ui.setupUi(NewProduct)
    NewProduct.show()
    sys.exit(app.exec_())
