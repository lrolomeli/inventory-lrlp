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

    def __init__(self, parent=None):
        super(NewProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.product = {}
        self.pushButton.clicked.connect(self.read_product)
        
    def read_product(self):
        
        if(self.lineEdit.text() == None or self.lineEdit_6.text()== None): 
            return
        self.product['name'] = self.lineEdit.text()
        self.product['category'] = self.lineEdit_3.text()
        self.product['color'] = self.lineEdit_6.text()
        self.product['location'] = self.lineEdit_5.text()
        self.product['cost'] = int(self.lineEdit_4.text())
        self.product['qty'] = int(self.lineEdit_2.text())
        # SEND EVENT DATA READY TO BE STORED
        self.close()

    def get_product(self):
        return self.product
        
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.inv_db = InventoryDB()
        self.show_all_items_in_stock()
        #self.show_items_list()
        self.pushButton.clicked.connect(self.openNewProductDialog)
        self.pushButton_2.clicked.connect(self.openProductSaleDialog)
        self.pushButton_3.clicked.connect(self.refreshProductTableContent)
        #self.tableWidget.doubleClicked.connect(self.openProductSaleDialog)


    def add_product(self, product):
        data = (product['name'], product['category'], product['color'], product['location'], product['cost'], product['qty'])
        self.inv_db.new_product(data)

    #    ['id'] = x[0]
    #    ['name'] = x[1]
    #    ['category'] = x[2]
    #    ['color'] = x[3]
    #    ['location'] = x[4]
    #    ['cost'] = x[5]
    #    ['qty'] = x[6]
    def refreshProductTableContent(self):
        # go to db and retrieve data
        
        self.inv_db.update_product_table()
        products = self.inv_db.get_product_table()
        self.tableWidget.setRowCount(len(products))
        row_index = 0
        for x in products:
            self.tableWidget.setItem(row_index,0,QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(row_index,1,QtWidgets.QTableWidgetItem(str(x[1])))
            self.tableWidget.setItem(row_index,2,QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(row_index,3,QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(row_index,4,QtWidgets.QTableWidgetItem(str(x[5])))
            self.tableWidget.setItem(row_index,5,QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(row_index,6,QtWidgets.QTableWidgetItem(str(x[6])))
            row_index += 1

    def show_all_items_in_stock(self):
        products = list()
        
        self.refreshProductTableContent()

    def show_items_list(self):
        self.inv_db.read_products()
        entries = ['one','two', 'three']
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def openNewProductDialog(self):
        w = NewProductDialog()
        w.exec_()
        self.add_product(w.get_product())
        
    def openProductSaleDialog(self):
        w = ProductSaleDialog()
        w.exec_()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryWindow = MainWindow()
    inventoryWindow.show()
    sys.exit(app.exec_())