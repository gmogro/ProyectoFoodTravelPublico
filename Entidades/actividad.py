class Actividad:

    def __init__(self,id,nombre,id_destino,hora_inicio):
        self.id = id
        self.nombre = nombre
        self.id_destino = id_destino
        self.hora_inicio = hora_inicio
    
    def __str__(self):
        return f"{self.nombre} - {self.id_destino} - {self.hora_inicio}"
    
    def to_json(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "id_destino" : self.id_destino,
            "hora_destino": self.hora_inicio
        }

    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        id_destino = data["id_destino"]
        hora_inicio = data["hora_inicio"]

        return Actividad(id,nombre,id_destino,hora_inicio)