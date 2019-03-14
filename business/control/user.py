import re

class User:
	def __init__(self, user_name, email, password):
		self.user_name = user_name
		self.email = email
		self.password = password

	def set_user_name(self, user_name):
		if len(user_name) == 0 or len(user_name) > 15:
			raise outOfBoundsUserNameException('User name is out of the specific range of 0~15 charactes')

		if bool(re.match('^(?=.*[0-9])', user_name)):
			raise incompatibleCharacterUserNameException('Contains a incompatible character')

		self.user_name = user_name

	def set_email(self, email):
		self.email = email

	def set_password(self, password):
		if (not bool(re.match('^(?=.*[0-9])', password)) and 
            not bool(re.match('^(?=.*[a-zA-Z])', password))):
			raise passwordMissingCharactersException('Missing a specif type of characters')

		if len(password) < 6 or 16 < len(password):
			raise outOfBoundsPasswordException('Password name is out of the specific range of 0~16 charactes')

		self.password = password

	def get_user_name(self):
		return self.user_name

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password



