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


def AtualizaOrcamento(nome, orcamento):
    DAO = RamOrcamentoDAO()

    Orcamento = DAO.busca_orcamento(id)
    Orcamento.nome = nome
    Orcamento.orcamento = orcamento
    
    DAO.atualiza_orcamento(orcamento)
        
    
