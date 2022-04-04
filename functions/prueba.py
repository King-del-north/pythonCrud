#importación modulo
import psycopg2

#conexión a base de datos

conexion = psycopg2.connect(user='postgres',
                            password='pucon',
                            host='127.0.0.1',
                            port='5432',
                            database='postgres'    
                            )
#Utilizar cursor                            
cursor = conexion.cursor()                  

#Crear sentencia SQL
sql = 'SELECT * FROM users'       

#Metodo execute
cursor.execute(sql)
registro= cursor.fetchall()

#funcion resultado
def listar():
    return registro

listar()
#cerrar conexion
cursor.close()
conexion.close()
