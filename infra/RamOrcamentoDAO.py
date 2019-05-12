import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.OrcamentoDAO import OrcamentoDAO
from business.model.Orcamento import Orcamento
from business.control.Exceptions.NotFoundException import NotFoundException


class RamOrcamentoDAO(OrcamentoDAO):
    def __init__(self):
        self.orcamento_list = []

    def insere_orcamento(self, orcamento: Orcamento):
        self.orcamento_list.append(orcamento)

    def atualiza_orcamento(self, orcamento: Orcamento):
        index = 0

        # Procura em cada elemento da lista:
        for orcamento_list_element in self.orcamento_list:
            # Caso encontre o Profisssional igual na lista:
            if orcamento_list_element == orcamento:
                # Remove a versão antiga
                self.orcamento_list.pop(index)
                # e adiciona a nova instância do objeto?
                self.orcamento_list.insert(index, orcamento)

                return None

            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("orcamento")

    def remove_orcamento(self, id):
        index = 0

        # Procura em cada elemento da lista:
        for orcamento in self.orcamento_list:
            # Caso encontre o Profisssional com o email fornecido
            if orcamento.get_id() == id:
                # Deleta ele e retorna seu valor:
                return self.orcamento_list.pop(index)
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for, retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("orcamento")

    def busca_orcamento(self, id):
        index = 0

        # Procura em cada elemento da lista:
        for orcamento in self.orcamento_list:
            # Caso encontre o Profisssional com o email fornecido
            if orcamento.get_id() == id:
                # Retorna o objeto encontrado:
                return orcamento
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("orcamento")