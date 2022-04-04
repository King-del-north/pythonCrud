from functions import prueba
from functions import insertar


menuprincipal= int(input("Menu Principal: \n 1-Listar usuarios \n 2-Agregar usuarios \n 3-Eliminar usuarios \n 0-Salir \n"))
while menuprincipal !=0:

    if menuprincipal == 1:
        print("Listando usuarios")
        print("################## \n")
        resultado=prueba.listar()
        print(resultado)
        
    elif menuprincipal == 2:
       name= input('Ingrese nombre: ')
       lastname= input('Ingrese apellido: ')
       age= input('Ingrese edad: ')
       datos=(name,lastname,age)
       insertar.insertarUsuarios(datos)
       
    elif menuprincipal == 3:
        pass
    elif menuprincipal == 4:
        pass
    else:
        print("Ingresa una opción correcta")
    
    menuprincipal= int(input("Menu Principal: \n 1-Listar usuarios \n 2-Agregar usuarios \n 3-Eliminar usuarios \n 0-Salir \n"))