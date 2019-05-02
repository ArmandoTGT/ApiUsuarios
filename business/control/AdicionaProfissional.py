import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	origin_path = "/.."
elif _platform == "win32" or "win64":
	origin_path = ".."

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.Validation.LoginValidation import LoginValidation
from business.control.Validation.PasswordValidation import PasswordValidation
from infra.infra import DBControl
from business.model.Profissional import Profissional
from infra.RamProfissionalDAO import RamProfissionalDAO


def AdicionaProfissional(id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco):
    email = LoginValidation().validate(email)
    
    senha = PasswordValidation().validate(senha)

    DAO = RamProfissionalDAO()
    
    #if DAO.validaEmail(email):
    profissional = Profissional(id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco)
    DAO.insere_profissional(profissional)
        
    #dbControl.closeDB()
