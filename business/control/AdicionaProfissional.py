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
from business.model.Profissional import Profissional
from infra.DAOFactory import DAOFactory


def AdicionaProfissional(profissional: Profissional):
    dao = DAOFactory.getDAOFactory("RAM").getProfissionalDAO()

    generated_id = str(uuid.uuid4()).split('-')
    final_id = str(profissional.get_cpf()) + generated_id[0] + generated_id[1]

    profissional.set_id(final_id)

    #profissional = ModelFactory.createObject("profissional", final_id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco)
    dao.insere_profissional(profissional)
