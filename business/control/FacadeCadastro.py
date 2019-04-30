import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	origin_path = "/.."
elif _platform == "win32" or "win64":
	origin_path = ".."

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.addUser import addUser
from business.control.Relatorios import Relatorios

class FacadeCadastro():
    cadastrou = 0

    def cadastroUsuario(self, nome, senha, email, dataNascimento, cpf):
        addUser(nome, senha, email, dataNascimento, cpf)
        cadastrou =+ 1

    
    def relatorio(self):
        Relatorios.relatorioHTML()
        Relatorios.relatorioXML()
        