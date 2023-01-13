
class Peliculas:
    def __init__(self, nombre:str):
        self.__nombre=nombre
        

    def __str__(self):
        return 'Pelicula: '+ self.__nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
        