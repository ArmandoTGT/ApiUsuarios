import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.model.Orcamento import Orcamento
from business.model.Profissional import Profissional
from business.control.FacadeCadastro import FacadeCadastro
from business.control.CommandAddOrcamento import CommandAddOrcamento
from business.control.CommandAddProfissional import CommandAddProfissional
from business.control.CommandGeraRelatorio import CommandGeraRelatorio
from business.control.CommandRelatorioAcesso import CommandRelatorioAcesso
from business.control.CommandValidaLogin import CommandValidaLogin
from business.control.CommandValidaProfissional import CommandValidaProfissional
from business.control.CommandValidaSenha import CommandValidaSenha


class Executor:
    def __init__(self, orcamento: Orcamento, profissional: Profissional, email: str, senha: str) -> None:
        self._orcamento = orcamento
        self._profissional = profissional
        self._email = email
        self._senha = senha
        self._tempo_decorrido = None
        self._commands = {}

        self._initiate_commands()

    def _initiate_commands(self):
        self._commands["add orcamento"] = CommandAddOrcamento(FacadeCadastro(), self._orcamento)
        self._commands["add profissional"] = CommandAddProfissional(FacadeCadastro(), self._profissional)
        self._commands["gera relatorio"] = CommandGeraRelatorio(FacadeCadastro(), self._tempo_decorrido)
        self._commands["acesso relatorio"] = CommandRelatorioAcesso(FacadeCadastro())
        self._commands["valida login"] = CommandValidaLogin(FacadeCadastro(), self._email)
        self._commands["valida senha"] = CommandValidaSenha(FacadeCadastro(), self._senha)
        self._commands["valida profissional"] = CommandValidaProfissional(FacadeCadastro(), self._email, self._senha)


