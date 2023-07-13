class Usuario:
    def __init__(self,id,nombre,apellido,historial_rutas = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_rutas is None:
            self.historial_rutas = []
        else:
            self.historial_rutas = historial_rutas
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
    def to_json(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "historial_rutas":self.historial_rutas
        }
    
    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        apellido = data["apellido"]
        historial_rutas = data["historial_rutas"]
        
        return Usuario(id,nombre,apellido,historial_rutas)