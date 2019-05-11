import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Command import Command
from business.control.FacadeCadastro import FacadeCadastro


class CommandGeraRelatorio(Command):
    def __init__(self, facade: FacadeCadastro, tempo_decorrido: int) -> None:
        self._facade = facade
        self._tempo_decorrido = tempo_decorrido

    def execute(self) -> None:
        self._facade.gera_relatorio(self._tempo_decorrido)
