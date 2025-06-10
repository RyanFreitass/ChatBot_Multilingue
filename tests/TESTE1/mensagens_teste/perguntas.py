from tkinter import Tk

class PerguntasUsuario:
    def __init__(self):
        # INÍCIO
        self.mensagens_inicio = [
            "Oi", "Olá","ola", "Ola" "Tudo bem?", "Oi, tudo bem?", "Bom dia", "Boa tarde", "Boa noite", # Portugues
            "Hi", "Hello", "How are you?", "Hi, how are you?", "Good morning", "Good afternoon", "Good evening", # Ingles
            "Hola", "¿Cómo estás?", "Hola, ¿cómo estás?", "Buenos días", "Buenas tardes", "Buenas noches", # Espanhol
            "Hallo", "Wie geht es dir?", "Hallo, wie geht es dir?", "Guten Morgen", "Guten Tag", "Guten Abend", # Alemao
            "Ciao", "Come stai?", "Ciao, come stai?", "Buongiorno", "Buon pomeriggio", "Buona sera" # Italiano
        ]
        self.mensagens_inicio = [palavra.upper() for palavra in self.mensagens_inicio] + \
                                [palavra.lower() for palavra in self.mensagens_inicio]

        # AJUDA
        self.mensagens_ajuda = [
            "Preciso de ajuda", "Ajuda", "Você pode me ajudar?", "Pode me ajudar?", "Estou com uma dúvida",
            "Dúvida", "O que devo fazer?" # Portugues
            "I need help", "Help", "Can you help me?", "Can you assist me?", "I have a question", # Ingles
            "Necesito ayuda", "Ayuda", "¿Puedes ayudarme?", "¿Puedes asistirme?", "Tengo una pregunta", # Espanhol
            "Ich brauche Hilfe", "Hilfe", "Kannst du mir helfen?", "Kannst du mir assistieren?", "Ich habe eine Frage", # Alemao
            "Ho bisogno di aiuto", "Aiuto", "Puoi aiutarmi?", "Puoi assistermi?", "Ho una domanda" # Italiano
        ]
        self.mensagens_ajuda = [palavra.upper() for palavra in self.mensagens_ajuda] + \
                               [palavra.lower() for palavra in self.mensagens_ajuda]


        # PASSAPORTE
        self.mensagens_passaporte = [
            "Passaporte", "Como faço para obter um passaporte?", "Quais são os documentos necessários para o passaporte?",
            "Preciso de ajuda no passaporte", # Portugues
            "Passport", "How do I get a passport?", "What documents are needed for the passport?", # Ingles
            "Pasaporte", "¿Cómo obtengo un pasaporte?", "¿Qué documentos se necesitan para el pasaporte?", # Espanhol
            "Pass", "Wie erhalte ich einen Pass?", "Welche Dokumente werden für den Pass benötigt?", # Alemao
            "Passaporto", "Come posso ottenere un passaporto?", "Quali documenti sono necessari per il passaporto?" # Italiano
        ]
        self.mensagens_passaporte = [palavra.upper() for palavra in self.mensagens_passaporte] + \
                                    [palavra.lower() for palavra in self.mensagens_passaporte]

        # CPF
        self.mensagens_cpf = [
            "CPF", "Como faço para obter um CPF?", "Quais são os documentos necessários para o CPF?",
            "Preciso de ajuda no CPF", # Portugues
            "CPF", "How do I get a CPF?", "What documents are needed for the CPF?", # Ingles
            "CPF", "¿Cómo obtengo un CPF?", "¿Qué documentos se necesitan para el CPF?", # Espanhol
            "CPF", "Wie erhalte ich ein CPF?", "Welche Dokumente werden für das CPF benötigt?", # Alemao
            "CPF", "Come posso ottenere un CPF?", "Quali documenti sono necessari per il CPF?" # Italiano
        ]
        self.mensagens_cpf = [palavra.upper() for palavra in self.mensagens_cpf] + \
                             [palavra.lower() for palavra in self.mensagens_cpf]


        # REGISTRO
        self.mensagens_registro = [
            "Registro", "Como faço para obter um registro?", "Quais são os documentos necessários para o registro?",
            "Preciso de ajuda no registro?", # Portugues
            "Register", "How do I get a registration?", "What documents are needed for registration?", # Ingles
            "Necesito ayuda con el registro", "Registro", "¿Cómo obtengo un registro?", "¿Qué documentos se necesitan para el registro?", # Espanhol
            "Registrierung", "Wie erhalte ich eine Registrierung?", "Welche Dokumente werden für die Registrierung benötigt?", # Alemao
            "Registrazione", "Come posso ottenere una registrazione?", "Quali documenti sono necessari per la registrazione?" # Italiano
        ]
        self.mensagens_registro = [palavra.upper() for palavra in self.mensagens_registro] + \
                                  [palavra.lower() for palavra in self.mensagens_registro]
        
        # IDIOMA
        self.mensagens_idioma = [
            "Idioma", "Como faço para alterar o idioma?", "Preciso de ajuda com o idioma", # Portgues
            "Language", "How can I change the language?", "I need help with the language", # Ingles 
            "Idioma", "¿Cómo cambio el idioma?", "Necesito ayuda con el idioma?", # Espanhol
            "Sprache", "Wie kann ich die Sprache ändern?", "Ich brauche Hilfe mit der Sprache", # Alemao
            "Lingua", "Come posso cambiare la lingua?", "Ho bisogno di aiuto con la lingua", # Italiano

            
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