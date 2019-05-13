import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    origin_path = "/.."
elif _platform == "win32" or "win64":
    origin_path = ".."

if origin_path not in sys.path:
    sys.path.append(origin_path)

import os

from business.control.Exceptions.WrongLoginException import WrongLoginException
from business.control.Exceptions.EmailAlreadyInUseException import EmailAlreadyInUseException
import shelve
import xml.etree.ElementTree
from django.core import serializers


class DBControl:
    def __init__(self):
         filename = os.path.dirname(os.path.abspath(__file__)) + "/Users.xml"
         self.__db = serializers.deserialize('xml',xml.etree.ElementTree.parse(filename))

    def checkUser(self, user_name, senha):
        if (user_name in list(self.__db.keys())) and (self.__db[user_name].getSenha() == senha):
            return True
        else:
            raise WrongLoginException

    def persisteUser(self, user):
        self.__db[user.getEmail()] = user
        return True

    def getUser(self, email):
        return self.__db[email]

    def excluiUser(self, email):
        del self.__db[email]
        return True

    def validaEmail(self, email):
        if email in list(self.__db.keys()):
            raise EmailAlreadyInUseException
        return True

    def closeDB(self):
        filename = os.path.dirname(os.path.abspath(__file__)) + "/Users.xml"
        self.__db = serializers.serialize('xml', self.__db)
        self.__db.close().write(filename)
        
