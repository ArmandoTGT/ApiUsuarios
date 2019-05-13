import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Validation.LoginValidation import LoginValidation
from business.control.Validation.PasswordValidation import PasswordValidation
from infra.RamProfissionalDAO import RamProfissionalDAO


def AtualizaProfissional(id, nome, senha, email, telefone, endereco):
    email = LoginValidation().validate(email)
    
    senha = PasswordValidation().validate(senha) 
    
    DAO = RamProfissionalDAO()

    profissional = DAO.busca_profissional_id(id)
    profissional.set_nome(nome)
    profissional.set_email(email)
    profissional.set_telefone(telefone)
    profissional.set_endereco(endereco)
    
    DAO.atualiza_profissional(profissional)
        
    
