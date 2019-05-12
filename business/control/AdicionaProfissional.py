import sys
import uuid

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Validation.LoginValidation import LoginValidation
from business.control.Validation.PasswordValidation import PasswordValidation
from business.model.Profissional import Profissional
from infra.RamProfissionalDAO import RamProfissionalDAO


def AdicionaProfissional(nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco):
    email = LoginValidation().validate(email)
    senha = PasswordValidation().validate(senha)

    DAO = RamProfissionalDAO()

    generate_id = str(uuid.uuid4()).split('-')
    id = str(cpf) + generate_id[0] + generate_id[1]

    profissional = Profissional(id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco)
    DAO.insere_profissional(profissional)
