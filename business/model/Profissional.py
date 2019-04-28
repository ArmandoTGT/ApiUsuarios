class Profissional:
    def __init__(self, id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh
        self.telefone = telefone
        self.endereco = endereco

    # Override do equals para fazer com que a comparação ==
    # entre dois objetos do tipo Profissional retorne True
    # caso os dois objetos possuam os mesmos atributos
    # que sejam únicos no sistema:
    def __eq__(self, other):
        # Basta que o email ou o CPF seja igual:
        # Nota: Caso um Profissional queira mudar algum atributo
        #       apenas poderá mudar um de cada vez pois isso
        #       garante que ao menos o email ou o CPF sejam
        #       iguais durante a comparação
        return self.id == other.id

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

