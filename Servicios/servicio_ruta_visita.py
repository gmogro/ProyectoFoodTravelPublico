from Entidades.ruta_visita import RutaVisita

class ServicioRutaVisita:

    def __init__(self):
        rutas = []
        with open("Persistencia/RutaVisita.json","r") as file:
            rutas_json = json.load(file)
        for data in rutas_json:
            rutas.append(RutaVisita.from_json(data))
        self.rutas = rutas
    
    def crearRuta(self,nombre,destinos):
        id = len(self.rutas) + 1 
        ruta = RutaVisita(id,nombre,destinos)
        self.rutas.append(ruta)
    
    def eliminarRuta(self,ruta):
        self.rutas.remove(ruta)
    
    def buscarRuta(self,id_ruta):
        for ruta in self.rutas:
            if ruta.id == id_ruta:
                return ruta
        return None
    
    def modificar(self,id_ruta,nombre,destinos):
        ruta = self.buscarRuta(id_ruta)
        if not(ruta is None):
            ruta.nombre = nombre
            ruta.destinos = destinos
        else:
            print("que no se encuentra la Ruta")
