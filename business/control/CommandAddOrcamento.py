import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Command import Command
from business.control.FacadeCadastro import FacadeCadastro
from business.model.Orcamento import Orcamento


class CommandAddOrcamento(Command):
    def __init__(self, facade: FacadeCadastro, orcamento: Orcamento) -> None:
        self._facade = facade
        self._orcamento = orcamento

    def execute(self) -> None:
        self._facade.add_orcamento(self._orcamento)
