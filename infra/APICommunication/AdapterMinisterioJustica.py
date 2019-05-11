import sys

from sys import platform as _platform
from infra.communication.adapter import Adaptador
from Mocks.mockMinisterioJustica import MinisterioJustica

class AdapterReceitaFederal(Adaptador):
    def __init__(self):
        self.__miniesterioJustica = MinisterioJustica()

    def operacao(self, rg, cpf):
        self.__ministerioJustica.AntecedenteCriminal(rg, cpf)