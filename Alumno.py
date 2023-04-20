'''

Ejemplo de como deberíamos de trabajar en un caso real.
Entidades = Tablas
Utilizamos librerias mas potentes que SQLLite -> framewors: 
Pasamos esquema de datos -> pasamos clases que sean espejo de la base de datos.

'''
class Alumno:
    def __init__(self,nombre,apellido,dni):
        try: 
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
        except Exception as e:
            print("Error",e)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre 
    

 