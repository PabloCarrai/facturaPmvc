import sqlite3

class gestorDb:
    def __init__(self):
        self.conexion=sqlite3.connect("factura.db")
        self.cursor=self.conexion.cursor()

    

