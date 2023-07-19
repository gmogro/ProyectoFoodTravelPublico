from Entidades.review import Review

class ServicioActividad:

    def __init__(self):
        reviews = []
        with open("Persistencia/Review.json","r") as file:
            reviews_json = json.load(file)
        for data in reviews_json:
            reviews.append(Review.from_json(data))
        self.reviews = reviews
    
    def crearReview(self,id_destino,id_usuario,calificacion,comentario,animo):
        id = len(self.reviews) + 1 
        review = Review(id,id_destino,id_usuario,calificacion,comentario,animo)
        self.reviews.append(review)
    
    def eliminarReview(self,review):
        self.reviews.remove(review)
    
    def buscarReview(self,id_review):
        for review in self.reviews:
            if review.id == id_review:
                return review
        return None
    
    def modificar(self,id_review,id_destino,id_usuario,calificacion,comentario,animo):
        review = self.buscarReview(id_review)
        if not(review is None):
            review.id_destino = id_destino
            review.id_usuario = id_usuario
            review.calificacion = calificacion
            review.comentario = comentario
            review.animo = animo
        else:
            print("que no se encuentra la Review")
