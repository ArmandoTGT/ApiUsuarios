from abc import ABC, abstractmethod
import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.model.Orcamento import Orcamento


class OrcamentoDAO(ABC):
    @abstractmethod
    def insere_orcamento(self, orcamento: Orcamento):
        pass

    @abstractmethod
    def atualiza_orcamento(self, orcamento: Orcamento):
        pass

    @abstractmethod
    def remove_orcamento(self, id):
        pass

    @abstractmethod
    def busca_orcamento(self, id):
        pass
