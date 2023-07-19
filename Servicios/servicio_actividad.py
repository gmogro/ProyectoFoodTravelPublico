from Entidades.actividad import Actividad

class ServicioActividad:

    def __init__(self):
        actividades = []
        with open("Persistencia/Actividad.json","r") as file:
            actividades_json = json.load(file)
            print(actividades_json)
        
        for data in actividades_json:
            actividades.append(Actividad.from_json(data))
        self.actividades = actividades
    
    def crearActividad(self,nombre,id_destino,hora_inicio):
        id = len(self.actividades) + 1 
        actividad = Actividad(id,nombre,id_destino,hora_inicio)
        self.actividades.append(actividad)
    
    def eliminarActividad(self,actividad):
        self.actividades.remove(actividad)
    
    def buscarActividad(self,id_actividad):
        for actividad in self.actividades:
            if actividad.id == id_actividad:
                return actividad
        return None
    
    def modificar(self,id_actividad):
        actividad = self.buscarActividad(id_actividad)
        if not(actividad is None):
            actividad.nombre = nombre
            actividad.id_destino = id_destino
            actividad.hora_inicio = hora_inicio
        else:
            print("que no se encuentra la Actividad")
