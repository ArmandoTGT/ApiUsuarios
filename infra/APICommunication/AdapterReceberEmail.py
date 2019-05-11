import sys

from sys import platform as _platform
from infra.communication.adapter import Adaptador
from Mocks.mockEmail import Email

class AdapterReceberEmail(Adaptador):

    def operacao(self):
        return Email().receberEmail()