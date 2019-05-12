import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Zelador import Zelador
from business.control.Fonte import Fonte


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
        self._fonte = Fonte(Profissional(id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco))
        self._zelador = Zelador(self._fonte)

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
        self._zelador.save_state(Profissional(self.id, self.nome, self.senha, self.email, self.data_nascimento,
                                              self.cpf, self.rg, self.cnh, self.telefone, self.endereco))
        self.nome = nome

    def set_senha(self, senha):
        self._zelador.save_state(Profissional(self.id, self.nome, self.senha, self.email, self.data_nascimento,
                                              self.cpf, self.rg, self.cnh, self.telefone, self.endereco))
        self.senha = senha

    def set_email(self, email):
        self._zelador.save_state(Profissional(self.id, self.nome, self.senha, self.email, self.data_nascimento,
                                              self.cpf, self.rg, self.cnh, self.telefone, self.endereco))
        self.email = email 

    def set_telefone(self, telefone):
        self._zelador.save_state(Profissional(self.id, self.nome, self.senha, self.email, self.data_nascimento,
                                              self.cpf, self.rg, self.cnh, self.telefone, self.endereco))
        self.telefone = telefone

    def set_endereco(self, endereco):
        self._zelador.save_state(Profissional(self.id, self.nome, self.senha, self.email, self.data_nascimento,
                                              self.cpf, self.rg, self.cnh, self.telefone, self.endereco))
        self.endereco = endereco

    def previous_state(self):
        self._zelador.undo_state()
        self._fonte = self._zelador.get_fonte()
        state = self._fonte.get_state()

        self.id = state.get_id()
        self.nome = state.get_nome()
        self.senha = state.get_senha()
        self.email = state.get_email()
        self.data_nascimento = state.get_data_nascimento()
        self.cpf = state.get_cpf()
        self.rg = state.get_rg()
        self.cnh = state.get_cnh()
        self.telefone = state.get_telefone()
        self.endereco = state.get_endereco()
