from tkinter import Tk
from perguntas import PerguntasUsuario

mensagens = PerguntasUsuario()
pergunta = input("Digite sua pergunta: ")

if pergunta in mensagens.get_mensagens_inicio():
    print("Olá! Como posso ajudar você hoje?")

elif pergunta in mensagens.get_mensagens_ajuda():
    print("Claro! Estou aqui para ajudar. O que você precisa saber?")

elif pergunta in mensagens.get_mensagens_passaporte():
    print("Para obter um passaporte, você precisa dos seguintes documentos...")

elif pergunta in mensagens.get_mensagens_cpf():
    print("Para obter um CPF, você precisa dos seguintes documentos...")

elif pergunta in mensagens.get_mensagens_registro():
    print("Para obter um registro, você precisa dos seguintes documentos...")

elif pergunta in mensagens.get_mensagens_idioma():
    print("Para alterar o idioma, você pode acessar as configurações do sistema e selecionar o idioma desejado.")

else:
    print("Desculpe, não entendi sua pergunta. Você pode reformular ou pedir ajuda de outra forma?")
