class Review:
    def __init__(self,id,id_destino,id_usuario,calificacion,comentario,animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
    
    def __str__(self):
        return f"{self.id_destino} - {self.id_usuario} - {self.calificacion} - {self.comentario} - {self.animo}"
    
    def to_json(self):
        return {
            "id" : self.id,
            "id_destino" : self.id_destino,
            "id_usuario" : self.id_usuario,
            "calificacion" : self.calificacion,
            "comentario" : self.comentario,
            "animo" : self.animo
        }

    @classmethod
    def from_json(cls,data):
        id = data["id"]
        id_destino = data["id_destino"]
        id_usuario = data["id_usuario"]
        calificacion = data["calificacion"]
        comentario = data["comentario"]
        animo = data["animo"]

        return Review(id,id_destino,id_usuario,calificacion,comentario,animo)
    