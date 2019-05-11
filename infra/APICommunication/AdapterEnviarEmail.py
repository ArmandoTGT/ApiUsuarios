import sys

from sys import platform as _platform
from infra.communication.adapter import Adaptador
from Mocks.mockEmail import Email

class AdapterEnviarEmail(Adaptador):

    def operacao(self, cpf, nascimento):
        Email().envioEmail(cpf, nascimento)