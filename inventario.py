import mysql.connector

class InventoryDB:

    def __init__(self):
        self.product_inventory = []
        self.db = mysql.connector.connect(host="localhost", user="root", password="root")
        self.cursor = self.db.cursor()
        self.create_inventariodb()
        
    def create_inventariodb(self):
        self.cursor.execute("SHOW DATABASES LIKE 'inventariodb';")
        row = self.cursor.fetchone()
        if(row == None):
            self.cursor.execute("CREATE DATABASE inventariodb;")
            self.cursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category VARCHAR(255), color VARCHAR(255) NOT NULL, location VARCHAR(255), cost int, qty int NOT NULL, UNIQUE (NAME));")
        else:        
            self.cursor.execute("USE inventariodb")
            self.cursor.execute("SHOW TABLES LIKE 'product';")
            row = self.cursor.fetchone()
            if(row == None):
                self.cursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category VARCHAR(255), color VARCHAR(255) NOT NULL, location VARCHAR(255), cost int, qty int NOT NULL, UNIQUE (NAME));")   
    
    def new_product(self, product_data):
        sql = "INSERT INTO product (name, category, color, location, cost, qty) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, product_data)
        self.db.commit()

    def update_product_table(self):
        self.product_inventory.clear()
        self.cursor.execute("SELECT * FROM product")
        result = self.cursor.fetchall()
        for x in result:
            self.product_inventory.append(x)

    def get_product_table(self):
        return self.product_inventory


    def product_sale(self):
        product_name = input('Producto Vendido: ')
        qty = int(input('cantidad de ventas: '))
        name = (product_name,)

        sql = "SELECT qty FROM product WHERE name = %s"
        self.cursor.execute(sql, name)
        result = self.cursor.fetchone()
        old_qty = int(result[0])
        print(old_qty)
        new_qty = str(old_qty-qty)
        sql = "UPDATE products SET qty = %s WHERE name = %s"
        val = (new_qty, product_name)
        self.cursor.execute(sql, val)
        self.db.commit()


    def delete_product(self):
        product_name = input('Ingresa el nombre del producto: ')
        sql = "DELETE FROM product WHERE name = %s"
        name = (product_name, )
        self.cursor.execute(sql, name)
        self.db.commit()
