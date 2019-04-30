class InvalidCPFExcption(Exception):
        
    def __str__(self):
        return "CPF ou Data de Nascimento invalido"