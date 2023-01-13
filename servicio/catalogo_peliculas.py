import os

class CatalogoPeliculas:
    ruta_archivo='peliculas.txt'
        
    @staticmethod
    def agregar_pelicula(pelicula):
        # nota personal: el archivo se crea por defecto en el mismo lugar donde se ejecuta el programa principal, en este caso se crea en donde este el archivo 'testeo.py'
        # a no ser que uno le especifique la direccion en donde crearse.
        try:
            archivo= open(CatalogoPeliculas.ruta_archivo,'a')
            archivo.write(pelicula.get_nombre() + '\n')
        except Exception as e:
            print('Ocurrio un error: ', e)
        finally:
            archivo.close()

    @staticmethod
    def listar_peliculas():
        try:
            archivo=open(CatalogoPeliculas.ruta_archivo, 'r')
            print(archivo.read())
        except Exception as e:
            print('Ocurrio un error: ', e)
        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print('Ocurrio un error: ', e)
        finally:
            print('Archivo eliminado: '+ CatalogoPeliculas.ruta_archivo)