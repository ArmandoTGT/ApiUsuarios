class WrongLoginException(Exception):
        
    def __str__(self):
        return "Usuario ou senha incorretos"