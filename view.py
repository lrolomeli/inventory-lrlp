from PySide2 import QtWidgets
from guiClass import *

class View:
    def __init__(self):
        #
        self.filter = {}

    def metodoprovisional(self):
        print("hola")
        #self.combobox_dict['category'] = self.main_window.category_filter_cb
        #self.combobox_dict['name'] = self.main_window.product_filter_cb
        

    def startApp(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        main_window.new_item_btn.clicked.connect(self.metodoprovisional)
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
            self.selected_category = self.category_filter_cb.currentText()
        if self.product_filter_cb.currentIndex():
            self.selected_product = self.product_filter_cb.currentText()
        # ...To Be Continued add more filters
        # evento listo

    def getFilter(self, filter):
        filter['category'] = self.selected_category
        filter['name'] = self.selected_product

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