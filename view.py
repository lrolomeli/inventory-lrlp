from PySide2 import QtWidgets
from main_window import Ui_MainWindow
from new_product_dialog import Ui_NewProduct
from edit_product_dialog import Ui_editProduct
from sale_dialog import Ui_sale_dialog


class ProductSaleDialog(QtWidgets.QDialog, Ui_sale_dialog):
    def __init__(self, parent=None):
        super(ProductSaleDialog, self).__init__(parent)
        self.setupUi(self)
        self.sale_btn.clicked.connect(self.product_sale)

    def product_sale(self):
        print("venta")

class EditProductDialog(QtWidgets.QDialog, Ui_editProduct):

    def __init__(self, parent=None):
        super(EditProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.product = {}
        self.update_product_btn.clicked.connect(self.edit_product)
        self.erase_btn.clicked.connect(self.erase_product)

    def edit_product(self):
        print("editando")

    def erase_product(self):
        print("borrando")

class NewProductDialog(QtWidgets.QDialog, Ui_NewProduct):

    def __init__(self, parent=None):
        super(NewProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.product = {}
        self.add_product_btn.clicked.connect(self.read_product)

    def read_product(self):
        if(self.name_txtedit.text() != None and self.color_txtedit.text() != None):
            self.product['name'] = self.ui.name_txtedit.text()
            self.product['category'] = self.ui.category_txtedit.text()
            self.product['color'] = self.color_txtedit.text()
            self.product['location'] = self.ui.location_txtedit.text()
            self.product['cost'] = int(self.cost_txtedit.text())
            self.product['qty'] = int(self.qty_txtedit.text())

        # SEND EVENT DATA READY TO BE STORED
        self.close()

    def get_product(self):
        return self.product

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setupDBConnection() # Inventory Configuration
        self.new_item_btn.clicked.connect(self.openNewProductDialog)
        self.outcome_btn.clicked.connect(self.openProductSaleDialog)
        self.income_btn.clicked.connect(self.openEditProductDialog)
        self.category_filter_cb.activated.connect(self.filterProductTable)        
        self.product_filter_cb.activated.connect(self.filterProductTable)
        self.actionLoadBackupFile.triggered.connect(self.load_backup_file)
        self.actionGenBackupFile.triggered.connect(self.generate_backup_file)

        # point to different function that edits the product fields
        self.inventory_table.doubleClicked.connect(self.openProductSaleDialog)    
    
    def openNewProductDialog(self):
        w = NewProductDialog()
        w.exec_()
        new_product = w.get_product()
        if new_product:
            self.add_product(new_product)

    def openEditProductDialog(self):
        w = EditProductDialog()
        w.exec_()

    def openProductSaleDialog(self):
        w = ProductSaleDialog()
        w.exec_()


class View:
    def __init__(self, window):
        #
        self.window = window
        self.filter = {}
        self.combobox_dict['category'] = self.category_filter_cb
        self.combobox_dict['name'] = self.product_filter_cb
        self.main_window = MainWindow()

    def startApp(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        self.main_window.show()
        sys.exit(app.exec_())

    def getPathFile(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '~/', '*.sql')


    def fill_combobox(self, filter, filtered_elements):
        combobox = self.combobox_dict[filter]
        combobox.addItem('')
        for filteredElement in filtered_elements:
            combobox.addItem(filteredElement[0])

    def filterTable(self):
        if self.category_filter_cb.currentIndex():
            self.filter['category'] = self.category_filter_cb.currentText()
        if self.product_filter_cb.currentIndex():
            self.filter['name'] = self.product_filter_cb.currentText()
        # ...To Be Continued add more filters
        # evento listo

    def getFilter(self):
        return self.filter

    def refreshTable(self, products):
        # update the other filter comboboxes
        # for example if filter category is fruta
        # we will show only products for category
        # fruta in combobox product to be implemented
        self.inventory_table.setRowCount(len(products))
        row_index = 0
        for x in products:
            self.inventory_table.setItem(
                row_index, 0, QtWidgets.QTableWidgetItem(str(x[1])))
            self.inventory_table.setItem(
                row_index, 1, QtWidgets.QTableWidgetItem(str(x[2])))
            self.inventory_table.setItem(
                row_index, 2, QtWidgets.QTableWidgetItem(str(x[3])))
            self.inventory_table.setItem(
                row_index, 3, QtWidgets.QTableWidgetItem(str(x[6])))
            self.inventory_table.setItem(
                row_index, 4, QtWidgets.QTableWidgetItem(str(x[5])))
            self.inventory_table.setItem(
                row_index, 5, QtWidgets.QTableWidgetItem(str(x[4])))
            row_index += 1