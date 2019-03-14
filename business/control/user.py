class User:

	def __init__(self, user_name, email, password):
		self.user_name = user_name
		self.email = email
		self.password = password

	def set_user_name(self, user_name):
		self.user_name = user_name

	def set_email(self, email):
		self.email = email

	def set_password(self, password):
		self.password = password

	def get_user_name(self):
		return self.user_name

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password



