import sys

from business.control
from business.control
import shelve

from business.model.cliente import Cliente

import re

filename = 'clientes.db'


def addCliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco):
	email = ValidaFormatoLogin().valida(email)
	senha = ValidaFormatoSenha().valida(senha)

	cliente = Cliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco)


## MANDAR O QUE TEM ABAIXO PRA INFRA DEPOIS
## TESTE
	db = shelve.open(filename, flag='c')
	db[email] = cliente
	db.close()