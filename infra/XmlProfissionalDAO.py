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
import os
import xml.etree.ElementTree
from django.core import serializers


class XmlProfissionalDAO(ProfissionalDAO):
    def __init__(self):
        filename = os.path.dirname(os.path.abspath(__file__)) + "/Users.xml"
        self.__db = serializers.deserialize('xml',xml.etree.ElementTree.parse(filename))


    def insere_profissional(self, profissional: Profissional):
        self.__db[profissional.get_id()] = profissional
        return True

    def atualiza_profissional(self, profissional: Profissional):
        self.__db[profissional.get_id()] = profissional
        return True

    def remove_profissional(self, profissional_id):
        del self.__db[profissional_id]
        return True

    def busca_profissional(self, profissional_id):
        return self.__db[profissional_id]
