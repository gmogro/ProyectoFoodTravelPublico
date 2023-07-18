from Entidades.destino_culinario import DestinoCulinario

class ServicioDestinoCulinario:

    def __init__(self):
        destinos = []
        with open("Persistencia/Destino.json","r") as file:
            destinos_json = json.load(file)
        
        for data in destinos_json:
            destinos.append(DestinoCulinario.from_json(data))
        self.destinos = destinos
    
    def crearDestinoCulinario(self):
        id = len(self.destinos) + 1 
        nombre = input("Ingrese el nombre : ")
        direccion = input("Ingrese la direccion : ")
        coordenadas = []
        for i in range(2):
            coordenadas.append(input("Ingrese la coordenada : "))
        ubicacion = Ubicacion(id,nombre,direccion,coordenadas)
        self.ubicaciones.append(ubicacion)
    
    def eliminarUbicacion(self,ubicacion):
        self.ubicaciones.remove(ubicacion)
    
    def buscarUbicacion(self,id_ubicacion):
        for ubicacion in self.ubicaciones:
            if ubicacion.id == id_ubicacion:
                return ubicacion
        return None
    
    def modificar(self,id_ubicacion):
        ubicacion = self.buscarUbicacion(id_ubicacion)
        if not(ubicacion is None):
            nombre = input("Ingrese el nombre : ")
            direccion = input("Ingrese la direccion : ")
            coordenadas = []
            for i in range(2):
                coordenadas.append(input("Ingrese la coordenada : "))
            ubicacion.nombre = nombre
            ubicacion.direccion = direccion
            ubicacion.coordenadas = coordenadas
        else:
            print("que no se encuentra la Ubicacion")
