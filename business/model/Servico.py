class Servico:
    # CONSTRUTOR:
    def __init__(self, id, nome: str, descricoes: str, cliente_nome: str, cliente_email: str):
        self.id = id
        self.nome = nome
        self.descricoes = descricoes
        self.cliente_nome = cliente_nome
        self.cliente_email = cliente_email
        self.orcamentos = []

    # Override do equals para fazer com que a comparação ==
    # entre dois objetos do tipo Profissional retorne True
    # caso os dois objetos possuam os mesmos atributos
    # que sejam únicos no sistema:
    def __eq__(self, other):
        return self.id == other.id

    # MÈTODOS GET:
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_descricoes(self):
        return self.descricoes

    def get_cliente_nome(self):
        return self.cliente_nome

    def get_cliente_email(self):
        return self.cliente_email

    def get_orcamentos(self):
        return self.orcamentos

    # MÈTODOS SET:
    def set_nome(self, nome):
        self.nome = nome

    def set_descricoes(self, descricoes):
        self.descricoes = descricoes

    def set_cliente_nome(self, cliente_nome):
        self.cliente_nome = cliente_nome

    def set_cliente_email(self, cliente_email):
        self.cliente_email = cliente_email

    def set_orcamentos(self, orcamentos):
        self.orcamentos = orcamentos

    # OUTROS MÉTODOS:
    def append_orcamento(self, orcamento):
        self.orcamentos.append(orcamento)
