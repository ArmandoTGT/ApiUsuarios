class Orcamento:
    # CONSTRUTOR:
    def __init__(self, id, nome: str, profissional, orcamento, idServico):
        self.__id = id
        self.__nome = nome
        self.__profissional = profissional
        self.__orcamento = orcamento
        self.__idServico = idServico

    # Override do equals para fazer com que a comparação ==
    # entre dois objetos do tipo Profissional retorne True
    # caso os dois objetos possuam os mesmos atributos
    # que sejam únicos no sistema:
    def __eq__(self, other):
        return self.__id == other.id

    # MÈTODOS GET:
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_profissional(self):
        return self.__profissional

    def get_orcamento(self):
        return self.__orcamento

    def get_idServico(self):
        return self.__id

    # MÈTODOS SET:
    def set_nome(self, nome):
        self.__nome = nome

    def set_orcamento(self, orcamento):
        self.__orcamento = orcamento
 