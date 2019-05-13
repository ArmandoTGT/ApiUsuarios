import sys
import threading
from datetime import datetime

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.AdicionaProfissional import AdicionaProfissional
from business.control.Validation.LoginValidation import LoginValidation
from business.control.Validation.PasswordValidation import PasswordValidation
from business.control.Exceptions.NotFoundException import NotFoundException
from business.model.Profissional import Profissional
from business.model.Orcamento import Orcamento

from infra.DAOFactory import DAOFactory


class FacadeCadastro:
    @staticmethod
    def add_profissional(nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco) -> None:
        global frequencia_de_acesso

        frequencia_de_acesso += 1

        FacadeCadastro.__relatorio_acesso()

        try:
            AdicionaProfissional(nome, senha, email, data_nascimento, cpf, rg, cnh, telefone, endereco)
        except Exception as E:
            print(E)

    @staticmethod
    def valida_login(email: str) -> str:
        global frequencia_de_acesso

        frequencia_de_acesso += 1

        FacadeCadastro.__relatorio_acesso()

        try:
            email = LoginValidation().validate(email.lower())
        except Exception as error:
            print('\n', error)

        return email

    @staticmethod
    def valida_senha(senha: str) -> str:
        global frequencia_de_acesso

        frequencia_de_acesso += 1

        FacadeCadastro.__relatorio_acesso()

        try:
            senha = PasswordValidation().validate(senha)
        except Exception as error:
            print('\n', error)

        return senha

    @staticmethod
    def valida_profissional(email: str) -> bool:
        global frequencia_de_acesso
        frequencia_de_acesso += 1

        FacadeCadastro.__relatorio_acesso()

        dao_profissional = DAOFactory.getDAOFactory("RAM").getProfissionalDAO()

        try:
            # Checa se o profissional já existe:
            dao_profissional.busca_profissional_email(email)
            # Se ele for encontrato, significa que há existe um usuário
            # com o mesmo email que esse novo que está tentando se cadastrar
            return False
        # Se ele lançar exceção, significa que o usuário ainda não
        # está registrado, ou seja, ele poderá ser registrado
        except NotFoundException:
            return True

    @staticmethod
    def save_logged_clients(email):
        global frequenciaDeAcesso
        frequenciaDeAcesso += 1
        # print('Frequencia de Acesso:', frequenciaDeAcesso)
        facade.relatorio_acesso()

        try:
            saveLoggedClients(email)
        except Exception as error:
            print('\n', error)

    @staticmethod
    def __relatorio_acesso():
        global horaPassada, tempoPassado

        horaAtual = datetime.now()

        tempoPassado = (horaAtual - horaPassada).seconds

        tempo = 10

        if tempoPassado > tempo:
            horaPassada = horaAtual
            threading.Timer(1, facade.gera_relatorio, args=[tempoPassado]).start()

    @staticmethod
    def gera_relatorio(tempoPassado):

        global frequenciaDeAcessoAnterior  # , tempoPassado

        # print('Gerando Relatório!')
        # print('Frequencia de Acesso:', frequenciaDeAcesso)
        # print('Frequencia de Acesso Anterior:', frequenciaDeAcessoAnterior)

        frequenciaAtual = (frequenciaDeAcesso - frequenciaDeAcessoAnterior)

        frequenciaDeAcessoAnterior = frequenciaDeAcesso

        # print('Frequencia Atual:', frequenciaAtual)
        # print('Tempo Passado:', tempoPassado)

        if frequenciaAtual == 0:
            quantidadeAcessoSegundos = (tempoPassado / 1)
        else:
            quantidadeAcessoSegundos = (tempoPassado / frequenciaAtual)

        # print('Quantidade Acesso Segundos:', quantidadeAcessoSegundos)

        minutosPassados = (tempoPassado / 60)

        dados = [frequenciaAtual, minutosPassados, quantidadeAcessoSegundos]

        relatorio('json').getRelatorio(dados)
