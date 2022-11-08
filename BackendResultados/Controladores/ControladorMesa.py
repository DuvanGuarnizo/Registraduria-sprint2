from Modelos.Mesa import Mesa

from Repositorios.MesaRepositorio import MesaRepositorio

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")
        self.mesaRepositorio = MesaRepositorio()

    def index(self):
        print("Listar todas las mesas")
        return self.mesaRepositorio.findAll()

    def create(self, laMesa):
        print("Crear una mesa")
        nuevaMesa = Mesa(laMesa)
        return self.mesaRepositorio.save(nuevaMesa)

    def show(self, id):
        print("Mostrando una mesa con id ", id)
        laMesa  = Mesa(self.mesaRepositorio.findById(id))
        return laMesa.__dict__

    def update(self, id, laMesa):
        print("Actualizando mesa con id ", id)
        mesaActual = Mesa(self.mesaRepositorio.findById(id))
        mesaActual.numero_Mesa = laMesa["numero_Mesa"]
        mesaActual.cantidad_inscritos = laMesa["cantidad_inscritos"]
        return self.mesaRepositorio.save(mesaActual)

    def delete(self, id):
        print("Elimiando mesa con id ", id)
        return self.mesaRepositorio.delete(id)