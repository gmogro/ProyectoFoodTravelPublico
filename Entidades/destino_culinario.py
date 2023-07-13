class DestinoCulinario:
    def __init__(self,id,nombre,tipo_cocina,precio_minimo,
                precio_maximo,popularidad,disponibilidad,id_ubicacion,
                imagen,ingredientes = None):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
        if ingredientes is None:
            self.ingredientes = []
        else:
            self.ingredientes = ingredientes
    
    def __str__(self):
        return f"{self.nombre} - {self.tipo_cocina} - {self.precio_minimo} - {self.precio_maximo} - {self.popularidad} - {self.disponibilidad}"
    
    def to_json(self):
        return {
            "id" : self.id,
            "nombre": self.nombre,
            "tipo_cocina" : self.tipo_cocina,
            "precio_minimo" : self.precio_minimo,
            "precio_maximo" : self.precio_maximo,
            "popularidad" : self.popularidad,
            "disponibilidad" : self.disponibilidad,
            "id_ubicacion" : self.id_ubicacion,
            "ingredientes" : self.ingredientes
        }
    
    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        tipo_cocina = data["tipo_cocina"]
        precio_minimo = data["precio_minimo"]
        precio_maximo = data["precio_maximo"]
        popularidad = data["popularidad"]
        disponibilidad = data["disponibilidad"]
        id_ubicacion = data["id_ubicacion"]
        ingredientes = data["ingredientes"]

        return DestinoCulinario(id,nombre,tipo_cocina,precio_minimo,precio_maximo,popularidad,disponibilidad,id_ubicacion,ingredientes)        
