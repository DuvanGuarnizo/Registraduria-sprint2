from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        self.candidatoRepositorio = CandidatoRepositorio()
        self.partidoRepositorio = PartidoRepositorio()

    """
    Relación partido candidato
    """

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.candidatoRepositorio.findById(id))
        partidoActual = Partido(self.partidoRepositorio.findById(id_partido))
        candidatoActual.Partido = partidoActual
        return self.candidatoRepositorio.save(candidatoActual)

    def index(self):
        print("Listar todos los candidatos")
        return self.candidatoRepositorio.findAll()

    def create(self, elCandidato):
        print("Crear un Candidato")
        nuevoCandidato = Candidato(elCandidato)
        return self.candidatoRepositorio.save(nuevoCandidato)

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = Candidato(self.candidatoRepositorio.findById(id))
        return elCandidato.__dict__

    def update(self, id, elCandidato):
        print("Actualizando candidato con id ", id)
        candidatoActual = Candidato(self.candidatoRepositorio.findById(id))
        candidatoActual.cedula = elCandidato["cedula"]
        candidatoActual.numero_resolucion = elCandidato["numero_resolucion"]
        candidatoActual.nombre = elCandidato["nombre"]
        candidatoActual.apellido = elCandidato["apellido"]
        return self.candidatoRepositorio.save(candidatoActual)

    def delete(self, id):
        print("Elimiando candidato con id ", id)
        return self.candidatoRepositorio.delete(id)