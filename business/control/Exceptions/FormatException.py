class FormatException(Exception):
    
    def __init__(self, descricaoFormatoCorreto : str):
        self.descricaoFormatoCorreto = descricaoFormatoCorreto
        
    def __str__(self):
        return "O formato usado é invalido, use o formato " + self.descricaoFormatoCorreto