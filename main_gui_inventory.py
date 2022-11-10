from PySide2 import QtCore, QtGui, QtWidgets

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
    def __init__(self, db, parent=None):
        super(NewProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_product)
        self.db = db
        
    def add_product(self):
        if(self.lineEdit.text() == None or self.lineEdit_6.text()== None): 
            return
        name = self.lineEdit.text()
        category = self.lineEdit_3.text()
        color = self.lineEdit_6.text()
        location = self.lineEdit_5.text()
        cost = int(self.lineEdit_4.text())
        qty = int(self.lineEdit_2.text())
        data = (name,category,color,location,cost,qty)
        print(data)
        self.db.new_product(data)
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.inv_db = InventoryDB()
        self.show_all_items_in_stock()
        #self.show_items_list()
        self.pushButton.clicked.connect(self.openNewProductDialog)
        self.pushButton_2.clicked.connect(self.openProductSaleDialog)
        #self.listView.doubleClicked.connect(self.openNewProductDialog)

    def show_all_items_in_stock(self):
        product = self.inv_db.read_products()
            
        #    ['id'] = x[0]
        #    ['name'] = x[1]
        #    ['category'] = x[2]
        #    ['color'] = x[3]
        #    ['location'] = x[4]
        #    ['cost'] = x[5]
        #    ['qty'] = x[6]
        self.tableWidget.setRowCount(len(product))
        row_index = 0
        for x in product:
            self.tableWidget.setItem(row_index,0,QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(row_index,1,QtWidgets.QTableWidgetItem(str(x[1])))
            self.tableWidget.setItem(row_index,2,QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(row_index,3,QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(row_index,4,QtWidgets.QTableWidgetItem(str(x[5])))
            self.tableWidget.setItem(row_index,5,QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(row_index,6,QtWidgets.QTableWidgetItem(str(x[6])))
            row_index += 1


    def show_items_list(self):
        self.inv_db.read_products()
        entries = ['one','two', 'three']
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def openNewProductDialog(self):
        w = NewProductDialog(self.inv_db)
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