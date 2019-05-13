from business.model.Profissional import Profissional
from business.model.Orcamento import Orcamento
from business.model.Servico import Servico

class ModelFactory():
    @staticmethod
    def createObject(objectType, *args):
      targetclass = objectType.capitalize()
      return globals()[targetclass](*args)

'''
user = ModelFactory.createObject("user",  user_name = "Armando",
                                 email = "armandotgt@gmail.com", password = "batman")
'''