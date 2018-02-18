class Pelicula:
    # Constructor de clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
        
    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se está borrando la película", self.titulo)
        
p = Pelicula("El Padrino",175,1972)
#del(p)