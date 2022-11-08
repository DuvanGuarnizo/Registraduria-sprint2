from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

from Repositorios.MesaRepositorio import MesaRepositorio
from Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

class ControladorResultado():

    def __init__(self):
        self.resultadoRepositorio = ResultadoRepositorio()
        self.mesaRepositorio = MesaRepositorio()
        self.candidatoRepositorio = CandidatoRepositorio()

    def index(self):
        return self.resultadoRepositorio.findAll()

    """
    Asignación mesa y candidato a resultado
    """

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.mesaRepositorio.findById(id_mesa))
        elCandidato = Candidato(self.candidatoRepositorio.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.resultadoRepositorio.save(nuevoResultado)


    def show(self, id):
        laResultado = Resultado(self.resultadoRepositorio.findById(id))
        return laResultado.__dict__

    """
    Modificación de resultado (mesa y candidato)
    """
    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.resultadoRepositorio.findById(id))
        elResultado.numero_mesa = infoResultado["numero_mesa"]
        elResultado.id_partido = infoResultado["id_partido"]
        laMesa = Mesa(self.mesaRepositorio.findById(id_mesa))
        elCandidato = Candidato(self.candidatoRepositorio.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.resultadoRepositorio.save(elResultado)

    def delete(self, id):
        return self.resultadoRepositorio.delete(id)

    def listarResultadosEnCandidato(self, id_candidato):
        return self.resultadoRepositorio.getListadoResultadosEnCandidato(id_candidato)