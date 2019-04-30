import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	origin_path = "/.."
elif _platform == "win32" or "win64":
	origin_path = ".."

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.Validation.Validation import Validation
from business.control.Validation.MockValidaCPF import consultarCPF
from business.control.Exceptions.InvalidCPFExcption import InvalidCPFExcption

class LoginValidation(Validation):
	def validate(self, cpf, dataNascimento):		
		
		if(not consultarCPF(cpf, dataNascimento)):
			raise InvalidCPFExcption()		