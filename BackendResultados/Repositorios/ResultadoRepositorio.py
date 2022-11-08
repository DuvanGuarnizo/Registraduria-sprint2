from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class ResultadoRepositorio(InterfaceRepositorio[Resultado]):

    def getListadoResultadosEnCandidato(self,id_candidato):
        theQuery = {"candidato.$id":ObjectId(id_candidato)}
        return self.query(theQuery)