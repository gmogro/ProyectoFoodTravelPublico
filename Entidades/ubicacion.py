class Ubicacion:
    def __init__(self,id,direccion,coordenadas = None):
        self.id = id
        self.direccion = direccion
        if coordenadas is None:
            self.coordenadas = []
        else:
            self.coordenadas = coordenadas
    
    def __str__(self):
        return f"{self.direccion} - {self.coordenadas}"
    
    def to_json(self):
        return {
            "id" : self.id,
            "direccion" : self.direccion,
            "coordenadas" : self.coordenadas
        }

    @classmethod
    def from_json(self,data):
        id = data["id"]
        direccion = data["direccion"]
        coordenadas = data["coordenadas"]

        return Ubicacion(id,direccion,coordenadas)
