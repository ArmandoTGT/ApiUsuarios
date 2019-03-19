import sys

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
