class FormatException(Exception):
    
    def __init__(self, descricaoFormatoCorreto : str):
        self.__descricaoFormatoCorreto = descricaoFormatoCorreto
        
    def __str__(self):
        return "O formato usado é invalido, use o formato " + self.__descricaoFormatoCorreto