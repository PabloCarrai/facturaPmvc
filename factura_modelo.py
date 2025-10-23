import sqlite3

class Factura:
    def __init__(self):
        self.conexion=sqlite3.connect("factura.db")
        self.cursor=self.conexion.cursor()

    

