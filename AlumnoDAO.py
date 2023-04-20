'''
AO = Data Access Object -> suministra interfaz común entre aplicación y base de datos-> interfaz que comunica nuestro de datos
con la base de datos.

este protgrama interactua entre los otros dos programas
conexion generada en main, se emplea en archivo alumnoDAO
'''

import sqlite3 
from Alumno import Alumno

class AlumnoDAO:

    def crear_tabla(con):
        try: 
            #Consultas multilinea
            sql = '''
                create table if not exists alumno(
                    nombre varchar (100),
                    apellido varchar (100),
                    dni varchar (10) primary key)
            
            '''
            cursor = con.cursor()
            cursor.execute(sql)
            print('La tabla ha sido creada')

        except Exception as e:
            print("Error1",e)

    def insertar_registro(con,Alumno):
        try: 
            #(???) -> se pasa como parámetros de la consulta -> se pasan como tuplas
            sql= '''
                insert into alumno values (?,?,?)   

            '''
            parametro = (Alumno.nombre,Alumno.apellido,Alumno.dni)
            cursor = con.cursor()
            cursor.execute(sql,parametro)
            con.commit()   #Solo para cuando hacemos transacciones(modificaciones de la BBDD)
            print("El registro se ha insertado correctamente")

        except Exception as e:
            print("Error2",e)


