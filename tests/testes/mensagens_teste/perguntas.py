from tkinter import Tk

class PerguntasUsuario:
    '''def mensagens(self):
        palavras_usuarios_inicio = [
            "Oi", "Olá", "Tudo bem?", "Oi, tudo bem?", "Bom dia", "Boa tarde", "Boa noite",
        ]
        palavras_usuarios_inicio = [palavra.upper() for palavra in palavras_usuarios_inicio] + \
                                   [palavra.lower() for palavra in palavras_usuarios_inicio]
        
        palavras_usuarios_ajuda = [
            "Preciso de ajuda", "Ajuda", "Você pode me ajudar?", "Pode me ajudar?", "Estou com uma dúvida",
            "Dúvida", "O que devo fazer?"
        ]
        palavras_usuarios_ajuda = [palavra.upper() for palavra in palavras_usuarios_ajuda] + \
                                  [palavra.lower() for palavra in palavras_usuarios_ajuda]                                

        palavras_usuarios_passaporte = [
            "Passaporte", "Como faço para obter um passaporte?", "Quais são os documentos necessários para o passaporte?"
            "Preciso de ajuda no passaporte"
        ]
        palavras_usuarios_passaporte = [palavra.upper() for palavra in palavras_usuarios_passaporte] + \
                                       [palavra.lower() for palavra in palavras_usuarios_passaporte]

        palavras_usuarios_cpf = [
            "CPF", "Como faço para obter um CPF?", "Quais são os documentos necessários para o CPF?",
            "Preciso de ajuda no CPF"
        ]
        palavras_usuarios_cpf = [palavra.upper() for palavra in palavras_usuarios_cpf] + \
                                [palavra.lower() for palavra in palavras_usuarios_cpf]

        palavras_usuarios_registro = [
            "Registro", "Como faço para obter um registro?", "Quais são os documentos necessários para o registro?",
            "Preciso de ajuda no registro"
        ]
        palavras_usuarios_registro = [palavra.upper() for palavra in palavras_usuarios_registro] + \
                                     [palavra.lower() for palavra in palavras_usuarios_registro]

        palavras_usuarios_idioma = [
            "Idioma", "Como faço para alterar o idioma?", "Preciso de ajuda com o idioma"
        ]
        palavras_usuarios_idioma = [palavra.upper() for palavra in palavras_usuarios_idioma] + \
                                   [palavra.lower() for palavra in palavras_usuarios_idioma]

        return palavras_usuarios_inicio + palavras_usuarios_ajuda + palavras_usuarios_passaporte + \
               palavras_usuarios_cpf + palavras_usuarios_registro + palavras_usuarios_idioma
    '''

    def __init__(self):
        # INÍCIO
        self.mensagens_inicio = [
            "Oi", "Olá", "Tudo bem?", "Oi, tudo bem?", "Bom dia", "Boa tarde", "Boa noite",
        ]
        self.mensagens_inicio = [palavra.upper() for palavra in self.mensagens_inicio] + \
                                [palavra.lower() for palavra in self.mensagens_inicio]

        # AJUDA
        self.mensagens_ajuda = [
            "Preciso de ajuda", "Ajuda", "Você pode me ajudar?", "Pode me ajudar?", "Estou com uma dúvida",
            "Dúvida", "O que devo fazer?"
        ]
        self.mensagens_ajuda = [palavra.upper() for palavra in self.mensagens_ajuda] + \
                               [palavra.lower() for palavra in self.mensagens_ajuda]


        # PASSAPORTE
        self.mensagens_passaporte = [
            "Passaporte", "Como faço para obter um passaporte?", "Quais são os documentos necessários para o passaporte?",
            "Preciso de ajuda no passaporte"
        ]
        self.mensagens_passaporte = [palavra.upper() for palavra in self.mensagens_passaporte] + \
                                    [palavra.lower() for palavra in self.mensagens_passaporte]

        # CPF
        self.mensagens_cpf = [
            "CPF", "Como faço para obter um CPF?", "Quais são os documentos necessários para o CPF?",
            "Preciso de ajuda no CPF"
        ]
        self.mensagens_cpf = [palavra.upper() for palavra in self.mensagens_cpf] + \
                             [palavra.lower() for palavra in self.mensagens_cpf]


        # REGISTRO
        self.mensagens_registro = [
            "Registro", "Como faço para obter um registro?", "Quais são os documentos necessários para o registro?",
            "Preciso de ajuda no registro"
        ]
        self.mensagens_registro = [palavra.upper() for palavra in self.mensagens_registro] + \
                                  [palavra.lower() for palavra in self.mensagens_registro]
        
        # IDIOMA
        self.mensagens_idioma = [
            "Idioma", "Como faço para alterar o idioma?", "Preciso de ajuda com o idioma"
        ]
        self.mensagens_idioma = [palavra.upper() for palavra in self.mensagens_idioma] + \
                                [palavra.lower() for palavra in self.mensagens_idioma]


    def get_mensagens_inicio(self):
        return self.mensagens_inicio
    
    def get_mensagens_ajuda(self):
        return self.mensagens_ajuda
    
    def get_mensagens_passaporte(self):
        return self.mensagens_passaporte
    def get_mensagens_cpf(self):
        return self.mensagens_cpf
    def get_mensagens_registro(self):
        return self.mensagens_registro
    def get_mensagens_idioma(self):
        return self.mensagens_idioma