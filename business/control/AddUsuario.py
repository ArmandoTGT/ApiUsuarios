from user import User

emailUsuario = input()
nomeUsuario = input()
senhaUsuario = input()

try:
	usuario = User(nomeUsuario, emailUsuario, senhaUsuario)
except outOfBoundsUserNameException:
	print('except')
except incompatibleCharacterUserNameException:
	print('except')
except passwordMissingCharactersException:
	print('except')
except outOfBoundsPasswordException:
	print('except')