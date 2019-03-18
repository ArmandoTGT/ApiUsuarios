from business.control.Validation.Validation import Validation
from business.control.Exceptions.MinLengthException import MinLengthException
from business.control.Exceptions.MaxLengthException import MaxLengthException
from business.control.Exceptions.FormatException import FormatException

class PasswordValidation(Validation):
	def validate(self, input_text):
		input_text_size = len(input_text)
		input_correct_format = any(character.isdigit() for character in input_text) and
                               not re.search('[a-zA-Z]', input_text) is None
		input_correct_length_min = 6 <= input_text_size 
		input_correct_length_max =      input_text_size <= 16
		
		if(not input_correct_length_min):
			raise MinLengthException(1, input_text_size)

		if(not input_correct_length_max):
			raise MaxLengthException(16, input_text_size)

		if(not input_correct_format):
			raise FormatException("Nome de usuário possuí algum caractere inválido.")