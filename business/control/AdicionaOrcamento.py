import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	origin_path = "/.."
elif _platform == "win32" or "win64":
	origin_path = ".."

if origin_path not in sys.path:
    sys.path.append(origin_path)

from infra.infra import DBControl
from business.model.Orcamento import Orcamento
from infra.RamOrcamentoDAO import RamOrcamentoDAO


def AdicionaOrcamento(id, nome, profissional, orcamento, idServico):

    DAO = RamOrcamentoDAO()    
   
    orcamento = Orcamento(id, nome, profissional, Orcamento, idServico)

    DAO.AdicionaOrcamento(orcamento)
        
   
