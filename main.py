from dominio.pelicula import Peliculas
from servicio.catalogo_peliculas import CatalogoPeliculas

print('Inicio del programa\n')

opcion=None
while opcion!='4':
    print('Opciones: ')
    print('1. Agregar pelicula')
    print('2. Listar peliculas')
    print('3. Eliminar archivo de peliculas')
    print('4. Salir')
    opcion=input('Ingrese una de las opciones mostradas: ')
    if opcion=='1':
        nom_peli=input('Ingrese el nombre de una pelicula: ')
        pelicula=Peliculas(nom_peli)
        CatalogoPeliculas.agregar_pelicula(pelicula)
        
    elif opcion=='2':
        CatalogoPeliculas.listar_peliculas()

    elif opcion=='3':
        CatalogoPeliculas.eliminar()
else:
    print('Programa terminado...')


