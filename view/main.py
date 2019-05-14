import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Validation.LoginValidation import LoginValidation
from business.control.Validation.PasswordValidation import PasswordValidation
from business.control.Exceptions.FormatException import FormatException
from business.control.Exceptions.MaxLengthException import MaxLengthException
from business.control.Exceptions.MinLengthException import MinLengthException
from business.control.Exceptions.WrongLoginException import WrongLoginException
from business.control.Command import Command
from infra.infra import DBControl
from getpass import getpass


class Lobby:
    def presentation():
        print('LOGIN:')

    def login():
        while(True):
            user_email = input('Email:')

            try:
                LoginValidation.validate(user_email)
                break
            except FormatException:
                print('O nome de usuário deve conter apenas letras')
            except MaxLengthException:
                print('O nome de usuário deve conter no máximo 16 letras')
            except MinLengthException:
                print('Nome de usuário não digitado')
            except Exception as e:
                print('Algo inesperado ocorreu, tente novamente.')
                print(e)

        while (True):
            user_password = getpass('Senha:')

            try:
                PasswordValidation.validate(user_password)
                break
            except FormatException:
                print('Para melhor protegê-lo, a senha deve conter letras e números')
            except MaxLengthException:
                print('A senha deve conter no máximo 15 caracteres')
            except MinLengthException:
                print('A senha deve conter no mínimo 6 caracteres')
            except Exception:
                print('Algo inesperado ocorreu, tente novamente.')

        try:
            DBControl.checkUser(user_name, user_password)
        except WrongLoginException:
            print('Nome de usuário já existente')


Lobby.presentation()
Lobby.login()

