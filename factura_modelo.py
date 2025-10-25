import sqlite3


class gestorDb:
    def abrir_conexion(self):
        try:
            self.conexion = sqlite3.connect("facturas_digitales.db")
            return self.conexion
        except:
            print("Error al conectar a la db")

    def registrar_Usuarios(self, datos):
        try:
            conexion = self.abrir_conexion()
            mycursor = conexion.cursor()
            sql = "insert into Clientes(nombre,apellido,email,telefono,direccion) values(?,?,?,?,?)"
            mycursor.execute(sql, datos)
            conexion.commit()
        finally:
            conexion.close()

    def listar_Usuarios(self):
        try:
            conexion = self.abrir_conexion()
            mycursor = conexion.cursor()
            sql = "select cliente_id,nombre,apellido from Clientes"
            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            return resultados
        finally:
            conexion.close()
