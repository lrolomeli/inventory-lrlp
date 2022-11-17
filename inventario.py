from PySide2 import QtCore, QtGui, QtWidgets

from new_product_dialog import Ui_NewProduct
from sale_dialog import Ui_Dialog
from main_window import Ui_MainWindow
from inventariodb import InventoryDB
from datetime import datetime
import os


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

        if(self.lineEdit.text() == None or self.lineEdit_6.text() == None):
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
        self.setupDBConnection()
        self.pushButton.clicked.connect(self.openNewProductDialog)
        self.pushButton_2.clicked.connect(self.openProductSaleDialog)
        self.pushButton_3.clicked.connect(self.refreshProductTable)

        self.product_cmbbox_2.activated.connect(self.filterProductTable)        
        self.product_cmbbox.activated.connect(self.filterProductTable)
        self.actionLoad_Backup_File.triggered.connect(self.load_backup_file)
        self.actionClose.triggered.connect(self.generate_backup_file)

        # point to different function that edits the product fields
        self.tableWidget.doubleClicked.connect(self.openProductSaleDialog)

    def setupDBConnection(self):
        try:
            self.inv_db = InventoryDB()
        except:
            print('No fue posible crear la conexion a mysql')
        else:
            try:
                self.inv_db.connect_to_database()
            except:
                print("No se encontro la base de datos")
            else:
                self.loadfilters()
                self.refreshProductTable()

    def load_backup_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '~/', '*.sql')
        cmd = 'mysql -u root < '+fname[0]
        print(cmd)
        result = os.system(cmd)
        if result == 0:
            self.inv_db.connect_to_database()
            self.loadfilters()
            self.refreshProductTable()

    def generate_backup_file(self):
        cmd = 'mysqldump -u root --add-drop-database --databases inventariodb > ~/Documents/Projects/Programming/inventory/inventariodb.sql'
        os.system(cmd)
        os.system('git add inventariodb.sql')
        date = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
        #os.system('git commit -m '+"\""+date+"\"")

    def filterProductTable(self):
        filter = {}
        if self.product_cmbbox_2.currentIndex():
            filter['category'] = self.product_cmbbox_2.currentText()
        if self.product_cmbbox.currentIndex():
            filter['name'] = self.product_cmbbox.currentText()
        # ...To Be Continued add more filters
        self.apply_filter(filter)

    def apply_filter(self, filter):
        self.inv_db.get_filtered_products(filter)
        products = self.inv_db.get_product_table()
        # update the other filter comboboxes
        # for example if filter category is fruta
        # we will show only products for category
        # fruta in combobox product to be implemented
        self.tableWidget.setRowCount(len(products))
        row_index = 0
        for x in products:
            self.tableWidget.setItem(
                row_index, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(
                row_index, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.tableWidget.setItem(
                row_index, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(
                row_index, 3, QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(
                row_index, 4, QtWidgets.QTableWidgetItem(str(x[5])))
            self.tableWidget.setItem(
                row_index, 5, QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(
                row_index, 6, QtWidgets.QTableWidgetItem(str(x[6])))
            row_index += 1

    def loadfilters(self):
        self.load_filter("category", self.product_cmbbox_2)
        self.load_filter("name", self.product_cmbbox)

    def load_filter(self, filterName, combobox):
        filtered_elements = []
        self.inv_db.get_column_no_duplicates(filterName, filtered_elements)
        combobox.addItem('')
        for filteredElement in filtered_elements:
            combobox.addItem(filteredElement[0])

    def add_product(self, product):
        data = (product['name'], product['category'], product['color'],
                product['location'], product['cost'], product['qty'])
        self.inv_db.new_product(data)
        self.filterProductTable()

    #    ['id'] = x[0]
    #    ['name'] = x[1]
    #    ['category'] = x[2]
    #    ['color'] = x[3]
    #    ['location'] = x[4]
    #    ['cost'] = x[5]
    #    ['qty'] = x[6]
    #  go to db and retrieve data
    def refreshProductTable(self):
        self.inv_db.update_product_table()
        products = self.inv_db.get_product_table()
        self.tableWidget.setRowCount(len(products))
        row_index = 0
        for x in products:
            self.tableWidget.setItem(
                row_index, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(
                row_index, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.tableWidget.setItem(
                row_index, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(
                row_index, 3, QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(
                row_index, 4, QtWidgets.QTableWidgetItem(str(x[5])))
            self.tableWidget.setItem(
                row_index, 5, QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(
                row_index, 6, QtWidgets.QTableWidgetItem(str(x[6])))
            row_index += 1

    def openNewProductDialog(self):
        w = NewProductDialog()
        w.exec_()
        new_product = w.get_product()
        if new_product:
            self.add_product(new_product)

    def openProductSaleDialog(self):
        w = ProductSaleDialog()
        w.exec_()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryWindow = MainWindow()
    inventoryWindow.show()
    sys.exit(app.exec_())
