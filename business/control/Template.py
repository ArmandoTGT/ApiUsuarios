import abc


class Template(metaclass=abc.ABCMeta):
  
    def template_method(self):
        self.relatorioXML()
        self.relatorioHTML()

    @abc.abstractmethod
    def relatorioHTML(self):
        pass

    @abc.abstractmethod
    def relatorioXML(self):
        pass