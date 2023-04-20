import sqlite3
from Alumno import Alumno
from AlumnoDAO import AlumnoDAO

con = None   #Declarar variable fuera del try en caso de que falle try, la variable se ha declarado anteriormente.

try: 
    #Creando la conexcion (si no existe archivo, crea uno)
    con=sqlite3.connect('./mydb.db')

    #Creando la tabla alumno
    AlumnoDAO.crear_tabla(con)

    #Crear alumnos
    alum1 = Alumno("Ruben","aa","xx")
    alum2 = Alumno("Alberto","bb","yy")

    #Insertar Alumnos en la BBDD
    AlumnoDAO.insertar_registro(con,alum1)
    AlumnoDAO.insertar_registro(con,alum2)
except Exception as e:
    print("Error3",e)



