import sys

from sys import platform as _platform
from infra.communication.adapter import Adaptador
from Mocks.mockReceitaFederal import ReceitaFederal

class AdapterReceitaFederal(Adaptador):
    def __init__(self):
        self.__receitaFederal = ReceitaFederal()
        
    def operacao(self, cpf, nascimento):
        self.__receitaFederal.validaCPF(cpf, nascimento)