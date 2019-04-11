import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.FactoryDAO import FactoryDAO
from business.model.User import User
from infra.infra import DBControl


class UserDAO(FactoryDAO):
    def get(self, id : str):
        DBControl.

    def get_all(self):
        pass

    def save(self, obj : User):
        pass

    def update(self, obj : User, new_obj : User):
        pass

    def delete(self, obj : User):
        pass