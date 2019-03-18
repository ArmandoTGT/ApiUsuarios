class MaxLengthException(Exception):
    def __init__(self, tamCerto : int, tamErrado : int):
        self.__tamCerto = tamCerto
        self.__tamErrado = tamErrado
        
    def __str__(self):
        return "O maximo de caracteres permitido é "+ self.__tamCerto +", Voçê usou" + self.__tamErrado