import mysql.connector

class Conecction:
    __host = "localhost"
    __user = "root"
    __password = ""
    __database = "moltodeli"
    connection = None

    def __init__(self):
        self.__host = self.__host
        self.__user = self.__user
        self.__password = self.__password
        self.__database = self.__database
        self.connection = self.connection
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )
            if self.connection.is_connected():
                print("Succefull Connection")
        except Exception as error:
            print("Error", error)

    def desconectar(self):
        try:
            if self.connection.is_connected():
                self.connection.disconnect()
                print("Disconnected")
        except:
            print("No connection")

    def consultaDB(self, consulta, tipoConsulta, parametros= None):
        cursor = self.connection.cursor()
        if parametros:
            if tipoConsulta == 1:
                cursor.execute(consulta, (parametros))
                self.connection.commit()
            else:
                cursor.execute(consulta, (parametros))
        else:
            cursor.execute(consulta)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados