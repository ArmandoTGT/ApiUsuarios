from abc import ABC, abstractmethod


class templateRelatorio(ABC):

    def relatorio(self, dados):
        print(self.geraRelatorio(dados))

    @abstractmethod
    def geraRelatorio(self, dados):
        pass