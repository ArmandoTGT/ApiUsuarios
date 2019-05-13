import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.RamOrcamentoDAO import RamOrcamentoDAO


def AtualizaOrcamento(nome, orcamento):
    DAO = RamOrcamentoDAO()

    Orcamento = DAO.busca_orcamento(id)
    Orcamento.set_nome(nome)
    Orcamento.set_orcamento(orcamento)
    
    DAO.atualiza_orcamento(orcamento)
        
    
