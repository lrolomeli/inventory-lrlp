from inventariodb import InventoryDB
from datetime import datetime
import os


class Model:

    def __init__(self):
        self.db = InventoryDB()

    def setupDBConnection(self):
        try:
            self.db = InventoryDB()
        except:
            print('No fue posible crear la conexion a mysql')
        else:
            try:
                self.db.connect_to_database()
            except:
                print("No se encontro la base de datos")
            else:
                self.loadfilters()
                self.refreshProductTable()

    def load_backup_file(self, fname):
        cmd = 'mysql -u root < '+fname[0]
        result = os.system(cmd)
        if result == 0:
            self.db.connect_to_database()
            self.loadfilters()
            self.refreshProductTable()

    def generate_backup_file(self):
        cmd = 'mysqldump -u root --add-drop-database --databases inventariodb > ~/Documents/Projects/Programming/inventory/inventariodb.sql'
        os.system(cmd)
        os.system('git add inventariodb.sql')
        date = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
        #os.system('git commit -m '+"\""+date+"\"")