from business.model.Profissional import Profissional
from business.model.Orcamento import Orcamento
from business.model.Servico import Servico
from business.model.User import User

class ModelFactory():
    @staticmethod
    def createObject(objectType, **kwargs):
      targetclass = objectType.capitalize()
      return globals()[targetclass]( **kwargs)

'''
user = ModelFactory.createObject("user",  user_name = "Armando",
                                 email = "armandotgt@gmail.com", password = "batman")
'''