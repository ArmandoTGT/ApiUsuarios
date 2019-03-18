class MinLengthException(Exception):
    def __init__(self, tamCerto : int, tamErrado : int):       
        self.__tamCerto = tamCerto
        self.__tamErrado = tamErrado
        
    def __str__(self):
        return "O minimo de caracteres permitido é "+ self.__tamCerto +", Voçê usou" + self.__tamErrado