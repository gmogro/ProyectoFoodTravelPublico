import json
from Entidades.destino_culinario import DestinoCulinario

class ServicioDestinoCulinario:

    def __init__(self):
        destinos = []
        with open("Persistencia/DestinoCulinarios.json","r") as file:
            destinos_json = json.load(file)
        
        for data in destinos_json:
            destinos.append(DestinoCulinario.from_json(data))
        self.destinos = destinos
    
    def crearDestinoCulinario(self,nombre,tipo_cocina,precio_minimo,
                precio_maximo,popularidad,disponibilidad,id_ubicacion,
                imagen,ingredientes = None):
        id = len(self.destinos) + 1 
        destino = DestinoCulinario(id,nombre,tipo_cocina,precio_minimo,
                precio_maximo,popularidad,disponibilidad,id_ubicacion,
                imagen,ingredientes)
        self.destinos.append(destino)
    
    def eliminarDestinoCulinario(self,destino):
        self.destinos.remove(destino)
    
    def buscarDestinoCulinario(self,id_destino):
        for destino in self.destinos:
            if destino.id == id_destino:
                return destino
        return None
    
    def modificar(self,id_destino,nombre,tipo_cocina,precio_minimo,
                precio_maximo,popularidad,disponibilidad,id_ubicacion,
                imagen,ingredientes):
        destino = self.buscarDestinoCulinario(id_destino)
        if not(destino is None):
            destino.nombre = nombre
            destino.tipo_cocina = tipo_cocina
            destino.precio_minimo = precio_minimo
            destino.precio_maximo = precio_maximo
            destino.popularidad = popularidad
            destino.disponibilidad = disponibilidad
            destino.id_ubicacion = id_ubicacion
            destino.imagen = imagen
            destino.ingredientes = ingredientes
        else:
            print("que no se encuentra Destino Culinario")

    def get_values(self):
        return self.destinos