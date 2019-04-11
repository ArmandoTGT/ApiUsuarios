import sys
from abc import ABC, abstractmethod

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.RamFactoryDAO import RamFactoryDAO
from infra.XmlFactoryDAO import XmlFactoryDAO

class FactoryDAO(ABC):
    @abstractmethod
    def get_userDAO(self):
        pass

    def get_FactoryDAO(self, factory_id):
        if factory_id == 'RAM Factory':
            return RamFactoryDAO



