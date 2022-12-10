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
        #self.setupDBConnection() # Inventory Configuration
        self.new_item_btn.clicked.connect(self.openNewProductDialog)
        self.outcome_btn.clicked.connect(self.openProductSaleDialog)
        self.income_btn.clicked.connect(self.openEditProductDialog)
        #self.category_filter_cb.activated.connect(self.filterProductTable)        
        #self.product_filter_cb.activated.connect(self.filterProductTable)
        #self.actionLoadBackupFile.triggered.connect(self.load_backup_file)
        #self.actionGenBackupFile.triggered.connect(self.generate_backup_file)

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