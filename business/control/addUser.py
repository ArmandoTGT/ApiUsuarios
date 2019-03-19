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
from business.model.User import User


def addUser(nome, senha, email):
    email = LoginValidation().validate(email)
    
    senha = PasswordValidation().validate(senha)

    dbControl = DBControl()
    
    if dbControl.validaEmail(email):
        cliente = User(nome, senha, email)
        dbControl.persisteUser(cliente)
        
    dbControl.closeDB()
