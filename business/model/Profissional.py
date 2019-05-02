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
   
    def get_nome(self):
        return self.nome

    def get_senha(self):
        return self.senha

    def get_email(self):
        return self.email

    def get_data_nascimento(self):
        return self.data_nascimento

    def get_cpf(self):
        return self.cpf

    def get_rg(self):
        return self.rg
    
    def get_cnh(self):
        return self.cnh

    def get_telefone(self):
        return self.telefone
    
    def get_endereco(self):
        return self.endereco
    
    def set_nome(self, nome):
        self.nome = nome

    def set_senha(self, senha):
        self.senha = senha

    def set_email(self, email):
        self.email = email 

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_endereco(self, endereco):
        self.endereco = endereco