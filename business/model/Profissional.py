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
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__email = email
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__cnh = cnh
        self.__telefone = telefone
        self.__endereco = endereco
        self.__fonte = Fonte(Profissional(id, nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco))
        self.__zelador = Zelador(self.__fonte)

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
        return self.__id == other.id

    def get_id(self):
        return self.__id
   
    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

    def get_email(self):
        return self.__email

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg
    
    def get_cnh(self):
        return self.__cnh

    def get_telefone(self):
        return self.__telefone
    
    def get_endereco(self):
        return self.__endereco
    
    def set_nome(self, nome):
        self.__zelador.save_state(Profissional(self.__id, self.__nome, self.__senha, self.__email, self.__data_nascimento,
                                               self.__cpf, self.__rg, self.__cnh, self.__telefone, self.__endereco))
        self.__nome = nome

    def set_senha(self, senha):
        self.__zelador.save_state(Profissional(self.__id, self.__nome, self.__senha, self.__email, self.__data_nascimento,
                                               self.__cpf, self.__rg, self.__cnh, self.__telefone, self.__endereco))
        self.__senha = senha

    def set_email(self, email):
        self.__zelador.save_state(Profissional(self.__id, self.__nome, self.__senha, self.__email, self.__data_nascimento,
                                               self.__cpf, self.__rg, self.__cnh, self.__telefone, self.__endereco))
        self.__email = email

    def set_telefone(self, telefone):
        self.__zelador.save_state(Profissional(self.__id, self.__nome, self.__senha, self.__email, self.__data_nascimento,
                                               self.__cpf, self.__rg, self.__cnh, self.__telefone, self.__endereco))
        self.__telefone = telefone

    def set_endereco(self, endereco):
        self.__zelador.save_state(Profissional(self.__id, self.__nome, self.__senha, self.__email, self.__data_nascimento,
                                               self.__cpf, self.__rg, self.__cnh, self.__telefone, self.__endereco))
        self.__endereco = endereco

    def previous_state(self):
        self.__zelador.undo_state()
        self.__fonte = self.__zelador.get_fonte()
        state = self.__fonte.get_state()

        self.__id = state.get_id()
        self.__nome = state.get_nome()
        self.__senha = state.get_senha()
        self.__email = state.get_email()
        self.__data_nascimento = state.get_data_nascimento()
        self.__cpf = state.get_cpf()
        self.__rg = state.get_rg()
        self.__cnh = state.get_cnh()
        self.__telefone = state.get_telefone()
        self.__endereco = state.get_endereco()
