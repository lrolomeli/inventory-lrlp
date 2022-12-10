import mysql.connector

class InventoryDB:

    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="root")
        self.product_inventory = []
        self.cursor = self.db.cursor()
        # Si no existe conexion a la base de datos
        # 

        # self.create_inventariodb()

    def use_inventariodb(self):
        self.cursor.execute("SHOW DATABASES LIKE 'inventariodb';")
        row = self.cursor.fetchone()
        if(row == None):
            return 0
        else:
            self.cursor.execute("USE inventariodb")
            return 1
            
    def connect_to_database(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="root", database="inventariodb")
        self.cursor = self.db.cursor()

    def new_product(self, product_data):
        sql = "INSERT INTO product (name, category, color, location, cost, qty) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, product_data)
        self.db.commit()

    def update_product_table(self, products):
        self.cursor.execute("SELECT * FROM product")
        result = self.cursor.fetchall()
        for x in result:
            products.append(x)

    def get_filtered_products(self, filter, products):
        filter_str = ""
        # Revisaremos cada elemento del diccionario y su valor
        for column in filter:
            filter_str += " && " + column +"= '"+ filter[column]+"'"

        query = "SELECT * FROM product WHERE qty >= 0"+filter_str
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for x in result:
            products.append(x)

    def get_column_no_duplicates(self, column_name, column_list):
        # TO DO: add where categoria = 'fruta' 
        sql = "SELECT "+column_name+" FROM product GROUP BY "+column_name 
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for x in result:
            column_list.append(x)


    def product_sale(self, productName, qty):
        # arguments
        # product_name
        element_list = (productName,)

        sql = "SELECT qty FROM product WHERE name = %s"
        self.cursor.execute(sql, element_list)
        result = self.cursor.fetchone()
        old_qty = int(result[0])
        print(old_qty)
        new_qty = str(old_qty-qty)
        sql = "UPDATE products SET qty = %s WHERE name = %s"
        element_list = (new_qty, productName)
        self.cursor.execute(sql, element_list)
        self.db.commit()


    def delete_product(self, productName):
        sql = "DELETE FROM product WHERE name = %s"
        element_list = (productName, )
        self.cursor.execute(sql, element_list)
        self.db.commit()
