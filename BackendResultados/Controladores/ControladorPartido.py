from Modelos.Partido import Partido
from Repositorios.PartidoRepositorio import PartidoRepositorio

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")
        self.partidoRepositorio = PartidoRepositorio()

    def index(self):
        print("Listar todos los partidos")
        return self.partidoRepositorio.findAll()

    def create(self, elPartido):
        print("Crear un Partido")
        nuevoPartido = Partido(elPartido)
        return self.partidoRepositorio.save(nuevoPartido)

    def show(self, id):
        print("Mostrando un Partido con id ", id)
        elPartido  = Partido(self.partidoRepositorio.findById(id))
        return elPartido.__dict__

    def update(self, id, elPartido):
        print("Actualizando Partido con id ", id)
        partidoActual = Partido(self.partidoRepositorio.findById(id))
        partidoActual.nombre = elPartido["nombre"]
        partidoActual.lema = elPartido["lema"]
        return self.partidoRepositorio.save(partidoActual)

    def delete(self, id):
        print("Elimiando Partido con id ", id)
        return self.partidoRepositorio.delete(id)