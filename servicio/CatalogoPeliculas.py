import os
class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.ruta_archivo,'a', encoding='UTF-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='UTF-8') as archivo:
            print('Catalogo de peliculas'.center(50, '*'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo {cls.ruta_archivo} eliminado')
