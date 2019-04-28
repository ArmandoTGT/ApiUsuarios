class NotFoundException(Exception):
    def __init__(self, element_name):
        self.element_name = element_name

    def __str__(self):
        return self.element_name + " não encontrado"