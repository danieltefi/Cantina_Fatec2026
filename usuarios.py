class Sistema: # implementa a proteção da senha (Encapsulamento)
    def __init__(self):
        self.__senhacorreta = 'atletica26' # senha privada para segurança

    def validar_senha(self, digitada):
        return digitada == self.__senhacorreta

class Usuario: # classe para guardar os dados de quem compra
    def __init__(self, nome, categoria, curso='N/A'):
        self.__nome = nome.capitalize()
        self.__categoria = categoria
        self.__curso = curso

    def get_nome(self): 
        return self.__nome # permitir a leitura dos dados
    def get_categoria(self): 
        return self.__categoria
    def get_curso(self): 
        return self.__curso