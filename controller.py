class Controller:

    def __init__(self, model, view):
        #
        self.model = model 
        self.view = view
        self.startApp()

        #self.view.eventofiltro.connects(self.applyfilter)

# Esta funcion debera iniciar 
    def startApp(self):
        self.view.startApp()

    def restore_inventario(self):
        path = self.view.getgetPathFile
        self.model.restore_db_from_file(path)

    def backup_inventario(self):
        self.model.generate_backup_file()


    def apply_filter(self):
        filter = {}
        products = []
        self.view.getFilter(filter)
        self.model.db.get_filtered_products(filter, products)
        self.view.refreshTable(products)
        products.clear()

    def load_filter(self, filterName):
        filtered_elements = []
        self.model.db.get_column_no_duplicates(filterName, filtered_elements)
        if filtered_elements:
            self.view.fill_combobox(filterName, filtered_elements)

    def loadfilters(self):
        self.load_filter("category")
        self.load_filter("name")


    def add_product(self, product):
        data = (product['name'], product['category'], product['color'],
                product['location'], product['cost'], product['qty'])
        self.model.db.new_product(data)
        self.view.filterTable()