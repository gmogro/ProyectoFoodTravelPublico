from Entidades.usuario import Usuario

class ServicioUsuario:

    def __init__(self):
        usuarios = []
        with open("Persistencia/Usuarios.json","r") as file:
            usuarios_json = json.load(file)
        for data in usuarios_json:
            usuarios.append(Usuario.from_json(data))
        self.usuarios = usuario
    
    def crearUsuario(self,nombre,apellido,historial_rutas = None):
        id = len(self.usuarios) + 1 
        usuario = Usuario(id,nombre,apellido,historial_rutas)
        self.usuarios.append(usuario)
    
    def eliminarUsuario(self,usuario):
        self.usuarios.remove(usuario)
    
    def buscarUsuario(self,id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    
    def modificar(self,id_usuario):
        usuario = self.buscarUsuario(id_usuario)
        if not(usuario is None):
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.historial_rutas = historial_rutas
        else:
            print("que no se encuentra el Usuario")
