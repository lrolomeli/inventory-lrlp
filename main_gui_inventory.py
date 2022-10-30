from PyQt5 import QtCore, QtGui, QtWidgets

from new_data_dialog import Ui_NewProduct
from sale_dialog import Ui_Dialog
from mainw_inventario import Ui_MainWindow
from inventario import InventoryDB

class ProductSaleDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(ProductSaleDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.product_sale)
        
    def product_sale(self):
        print("venta")
        
class NewProductDialog(QtWidgets.QDialog, Ui_NewProduct):
    def __init__(self, text, parent=None):
        super(NewProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText(text)
        self.pushButton.clicked.connect(self.add_product)
        
    def add_product(self):
        if(self.lineEdit.text() == None or self.lineEdit_6.text()== None): 
            return
        inv_db = InventoryDB()
        name = self.lineEdit.text()
        category = self.lineEdit_3.text()
        color = self.lineEdit_6.text()
        location = self.lineEdit_5.text()
        cost = int(self.lineEdit_4.text())
        qty = int(self.lineEdit_2.text())
        data = (name,category,color,location,cost,qty)
        print(data)
        inv_db.new_product(data)
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show_all_items_in_stock()
        self.pushButton.clicked.connect(self.openNewProductDialog)
        self.pushButton_2.clicked.connect(self.openProductSaleDialog)
        self.listView.doubleClicked.connect(self.openNewProductDialog)

    def show_all_items_in_stock(self):
        entries = ['one','two', 'three']
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def openNewProductDialog(self):
        data = self.lineEdit.text()
        w = NewProductDialog(data)
        w.exec_()
        
    def openProductSaleDialog(self):
        w = ProductSaleDialog()
        w.exec_()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryWindow = MainWindow()
    inventoryWindow.show()
    sys.exit(app.exec_())