import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from infra.DAOFactory import DAOFactory
from infra.XmlProfissionalDAO import XmlProfissionalDAO as XmlProfissionalDAO
from infra.XmlServicoDAO import XmlServicoDAO as XmlServicoDAO

class XmlDAOFactory(DAOFactory):
    def getProfissionalDAO(self):
        return XmlProfissionalDAO

    def getServicoDAO(self):
        return XmlServicoDAO