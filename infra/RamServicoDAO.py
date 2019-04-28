from abc import ABC, abstractmethod
import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Exceptions.NotFoundException import NotFoundException
from business.model.Servico import Servico
from infra.ServicoDAO import ServicoDAO


class RamServicoDAO(ServicoDAO):
    def __init__(self):
        self.servico_list = []

    def atualiza_servico(self, servico: Servico):
        index = 0

        # Procura em cada elemento da lista:
        for servico_list_element in self.servico_list:
            # Caso encontre o Serviço igual na lista?
            if servico_list_element == servico:
                # Remove a versão antiga
                self.servico_list.pop(index)
                # e adiciona a nova instância do objeto?
                self.servico_list.insert(index, servico)

            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")

    def busca_servico(self, id):
        index = 0

        # Procura em cada elemento da lista:
        for servico in self.servico_list:
            # Caso encontre o Serviço com o email fornecido
            if servico.get_id() == id:
                # Retorna o objeto encontrado:
                return servico
            
            # Incrementa o índice:
            index += 1

        # Caso passe pelo for retorna uma exceção
        # indicando que a operação Falhou
        raise NotFoundException("profissional")
