from tkinter import Tk
from perguntas import PerguntasUsuario

mensagens = PerguntasUsuario()

if "Quem" in mensagens.mensagens():
    print("A palavra 'Quem' está na lista de mensagens.")