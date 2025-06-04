import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class ConsuladoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Atendimento Consular Inteligente")
        self.translator = Translator()
        self.language = 'pt'  # idioma padrão

        self.setup_ui()

    def setup_ui(self):
        self.label_title = tk.Label(self.root, text="Bem-vindo ao Consulado", font=("Arial", 18))
        self.label_title.pack(pady=10)

        self.btn_passaporte = tk.Button(self.root, text="Solicitar Passaporte", command=self.acao_passaporte)
        self.btn_passaporte.pack(pady=5)

        self.btn_registro = tk.Button(self.root, text="Registro Civil", command=self.acao_registro)
        self.btn_registro.pack(pady=5)

        self.btn_cpf = tk.Button(self.root, text="Criar CPF", command=self.acao_cpf)
        self.btn_cpf.pack(pady=5)

        self.language_selector = ttk.Combobox(self.root, values=["Português", "Inglês", "Espanhol", "Alemão", "Italiano"])
        self.language_selector.current(0)
        self.language_selector.pack(pady=5)
        self.language_selector.bind("<<ComboboxSelected>>", self.translate_interface)

        # Chatbot simples
        self.chatbox = tk.Text(self.root, height=10, width=50)
        self.chatbox.pack(side=tk.BOTTOM, pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.send_btn = tk.Button(self.root, text="Enviar", command=self.process_chat)
        self.send_btn.pack(side=tk.RIGHT, padx=5)

    def acao_passaporte(self):
        self.chatbox.insert(tk.END, "Você escolheu: Solicitar Passaporte\n")

    def acao_registro(self):
        self.chatbox.insert(tk.END, "Você escolheu: Registro Civil\n")

    def acao_cpf(self):
        self.chatbox.insert(tk.END, "Você escolheu: Criar CPF\n")

    def translate_interface(self, event=None):
        idioma_map = {
            "Português": "pt",
            "Inglês": "en",
            "Espanhol": "es",
            "Alemão": "de",
            "Italiano": "it"
        }
        escolha = self.language_selector.get()
        self.language = idioma_map[escolha]

        for widget in [self.label_title, self.btn_passaporte, self.btn_registro, self.btn_cpf]:
            texto_original = widget.cget("text")
            try:
                traducao = self.translator.translate(texto_original, src='pt', dest=self.language).text
                widget.config(text=traducao)
            except Exception as e:
                print(f"Erro na tradução: {e}")

    def process_chat(self):
        pergunta = self.entry.get()
        self.chatbox.insert(tk.END, f"Usuário: {pergunta}\n")
        # Resposta simples
        resposta = self.responder(pergunta)
        self.chatbox.insert(tk.END, f"Bot: {resposta}\n")
        self.entry.delete(0, tk.END)

    def responder(self, pergunta):
        pergunta = pergunta.lower()
        if "passaporte" in pergunta:
            return "Para passaportes, clique no botão 'Solicitar Passaporte'."
        elif "registro" in pergunta:
            return "O serviço de Registro Civil cobre nascimento, casamento e óbito."
        elif "cpf" in pergunta:
            return "Para criar um CPF, clique no botão 'Criar CPF'."
        elif "idioma" in pergunta or "traduzir" in pergunta:
            return "Você pode trocar o idioma no menu suspenso acima."
        else:
            return "Desculpe, não entendi. Pode reformular?"

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = ConsuladoApp(root)
    root.mainloop()