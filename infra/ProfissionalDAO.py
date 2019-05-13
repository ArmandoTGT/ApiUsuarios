from abc import ABC, abstractmethod
import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.model.Profissional import Profissional


class ProfissionalDAO(ABC):
    @abstractmethod
    def insere_profissional(self, profissional: Profissional):
        pass

    @abstractmethod
    def atualiza_profissional(self, profissional: Profissional):
        pass

    @abstractmethod
    def remove_profissional(self, profissional_id):
        pass

    @abstractmethod
    def busca_profissional_id(self, profissional_id: str) -> Profissional:
        pass

    @abstractmethod
    def busca_profissional_email(self, email: str) -> Profissional:
        pass
