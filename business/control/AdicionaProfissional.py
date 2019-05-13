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
from business.model.ModelFactory import ModelFactory
from infra.RamProfissionalDAO import RamProfissionalDAO


def AdicionaProfissional(nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco):
    email = LoginValidation().validate(email)
    senha = PasswordValidation().validate(senha)

    DAO = RamProfissionalDAO()

    generated_id = str(uuid.uuid4()).split('-')
    final_id = str(cpf) + generated_id[0] + generated_id[1]

    profissional = ModelFactory.createObject("profissional", final_id, nome, senha, email,
                                             data_nascimento, cpf, rg, cnh, telefone, endereco)
    DAO.insere_profissional(profissional)
