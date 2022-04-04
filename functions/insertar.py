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
sql = 'INSERT INTO users(name,lastname,age) VALUES(%s,%s,%s)'  

#mensaje para usuarios
def insertarUsuarios(datos):       
     #hacer uso del metodo execute
    cursor.execute(sql,datos)

    #guardar registro
    conexion.commit()

    #registro insertados
    registros = cursor.rowcount

    mensaje = print(f'registro insertado: {registros}')
    return mensaje

insertarUsuarios()

#cerrar conexiones
cursor.close()
conexion.close()






