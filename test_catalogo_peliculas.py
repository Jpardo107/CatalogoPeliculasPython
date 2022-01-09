from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('opciones:'.center(50,'*'))
        print('1 Agregar pelicula')
        print('2 Listar pelicula')
        print('3 Eliminar pelicula')
        print('4 Salir')
        opcion = int(input('Ingrese una opcion entre 1 y 4: '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese un nombre: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregarPelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa'.center(50,'*'))