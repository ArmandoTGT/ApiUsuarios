import sys

import pickle
import collections
from datetime import datetime

from business.model.User import User
from infra import DBControl

def loadLoggedUsers():
    try:
        with open('loggedUsers.pck', 'rb') as arq:
            dict_log = pickle.load(arq)
            arq.close()
    except Exception:
        return collections.OrderedDict()

    return dict_log

def saveLoggedUsers(email):

    dict_log = loadLoggedUsers()

    dbCrontol = DBControl()

    dict_log[email] = dbCrontol.getUser(email)

    with open('loggedUsers.pck', 'wb') as arq:
        pickle.dump(dict_log, arq, pickle.HIGHEST_PROTOCOL)
        arq.close()

    printLoggedUsers()

def printLoggedUsers():
    dict_log = loadLoggedUsers()

    list = []
    for user in dict_log:
        data = dict_log[user].getNascimento()
        list.append((data, dict_log[user].getNome()))

    list.sort(key=lambda date: datetime.strptime(date[0], "%d/%m/%Y"))

    print('\nLista Ordenada:', list)

def deleteLoggedUsers(email):

    dict_log = loadLoggedUsers()
    del dict_log[email]

    with open('loggedUsers.pck', 'wb') as arq:
        pickle.dump(dict_log, arq, pickle.HIGHEST_PROTOCOL)
        arq.close()
    printLoggedUsers()
