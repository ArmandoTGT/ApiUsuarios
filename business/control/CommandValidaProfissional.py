import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Command import Command
from business.control.FacadeCadastro import FacadeCadastro
from business.control.Exceptions.AlreadyInUseException import AlreadyInUseException


class CommandValidaProfissional(Command):
    def __init__(self, facade: FacadeCadastro, email: str, senha: str) -> None:
        self._facade = facade
        self._senha = senha
        self._email = email

    def execute(self) -> None:
        is_valid = self._facade.valida_profissional(self._email)

        if not is_valid:
            raise AlreadyInUseException("email")
