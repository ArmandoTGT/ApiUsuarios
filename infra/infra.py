import os
import sys

from business.control.Exceptions.WrongLoginException import WrongLoginException
from business.control.Exceptions.EmailAlreadyInUseException import EmailAlreadyInUseException
import shelve

from business.model.User import User


class DBControl:
    def __init__(self):
         filename = os.path.dirname(os.path.abspath(__file__)) + "/Users.db"
         self.__db = shelve.open(filename, flag='c')

    def CheckUser(self, email, senha):

        if (email in list(self.__db.keys())) and (self.__db[email].getSenha() == senha):
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
        self.__db.close()
