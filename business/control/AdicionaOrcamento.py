import sys
import uuid

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.model.ModelFactory import ModelFactory
from infra.RamOrcamentoDAO import RamOrcamentoDAO


def AdicionaOrcamento(nome, profissional, orcamento, id_servico):
    DAO = RamOrcamentoDAO()

    generated_id = str(uuid.uuid4()).split('-')
    final_id = str(id_servico) + generated_id[0] + generated_id[1]
   
    orcamento = ModelFactory.createObject("orcamento", final_id, nome, profissional, orcamento, id_servico)

    DAO.insere_orcamento(orcamento)
