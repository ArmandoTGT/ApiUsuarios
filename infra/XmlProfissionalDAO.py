import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.ProfissionalDAO import ProfissionalDAO
from business.model.Profissional import Profissional
from business.control.Exceptions.NotFoundException import NotFoundException


class RamProfissionalDAO(ProfissionalDAO):
    def __init__(self):
        pass

    def insert_profissional(self, profissional: Profissional):
        pass

    def delete_profissional(self, email: str):
        pass

    def update_profissional(self, profissional: Profissional):
        pass

    def find_profissional(self, email: str):
        pass