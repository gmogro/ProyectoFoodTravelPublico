from Entidades.actividad import Actividad

class ServicioActividad:

    def __init__(self):
        actividades = []
        with open("Persistencia/Actividad.json","r") as file:
            actividades_json = json.load(file)
            print(actividades_json)
        w
        for data in actividades_json:
            actividades.append(Actividad.from_json(data))
        self.actividades = actividades
    
    def crearUbicacion(self):
        id = len(self.ubicaciones) + 1 
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
