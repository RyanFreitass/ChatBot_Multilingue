import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
from mensagens_teste.perguntas import PerguntasUsuario

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

        self.btn_cpf = tk.Button(self.root, text="Cadastro CPF", command=self.acao_cpf)
        self.btn_cpf.pack(pady=5)

        self.language_selector = ttk.Combobox(
            self.root,
            values=["Português", "Inglês", "Espanhol", "Alemão", "Italiano"]
        )
        self.language_selector.current(0)
        self.language_selector.pack(pady=5)
        self.language_selector.bind("<<ComboboxSelected>>", self.translate_interface)

        # Chatbot simples
        self.chatbox = tk.Text(self.root, height=10, width=60)
        self.chatbox.pack(pady=10)
        self.chatbox.config(state='disabled')

        self.entry = tk.Entry(self.root, width=45)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.send_btn = tk.Button(self.root, text="Enviar", command=self.process_chat)
        self.send_btn.pack(side=tk.RIGHT, padx=5)

    # ======= FORMULÁRIOS =======

    def acao_passaporte(self):
        form = tk.Toplevel(self.root)
        form.title("Formulário de Solicitação de Passaporte")

        tk.Label(form, text="Nome Completo:").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="Data de Nascimento (DD/MM/AAAA):").pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text="Número de Identidade (RG):").pack()
        rg_entry = tk.Entry(form)
        rg_entry.pack()

        tk.Label(form, text="E-mail para contato:").pack()
        email_entry = tk.Entry(form)
        email_entry.pack()

        def enviar_formulario():
            nome = nome_entry.get()
            data = data_entry.get()
            rg = rg_entry.get()
            email = email_entry.get()
            print(f"Solicitação de passaporte enviada para {nome} - {email}")
            messagebox.showinfo("Sucesso", "Formulário enviado com sucesso!")

        tk.Button(form, text="Enviar", command=enviar_formulario).pack(pady=10)

    def acao_registro(self):
        form = tk.Toplevel(self.root)
        form.title("Formulário de Registro Civil")

        tk.Label(form, text="Tipo de Registro:").pack()
        tipo_var = tk.StringVar()
        tipo_combobox = ttk.Combobox(form, textvariable=tipo_var, values=["Nascimento", "Casamento", "Óbito"])
        tipo_combobox.pack()

        tk.Label(form, text="Nome Completo:").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="Data do Evento (DD/MM/AAAA):").pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text="Local do Evento:").pack()
        local_entry = tk.Entry(form)
        local_entry.pack()

        tk.Label(form, text="Nome dos Pais (se aplicável):").pack()
        pais_entry = tk.Entry(form)
        pais_entry.pack()

        def enviar_formulario():
            tipo = tipo_var.get()
            nome = nome_entry.get()
            data = data_entry.get()
            local = local_entry.get()
            pais = pais_entry.get()
            print(f"Registro de {tipo} para {nome} enviado.")
            messagebox.showinfo("Sucesso", f"Formulário de {tipo} enviado com sucesso!")

        tk.Button(form, text="Enviar", command=enviar_formulario).pack(pady=10)

    def acao_cpf(self):
        form = tk.Toplevel(self.root)
        form.title("Formulário de Solicitação de CPF")

        tk.Label(form, text="Nome Completo:").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="Data de Nascimento (DD/MM/AAAA):").pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text="Nome da Mãe:").pack()
        mae_entry = tk.Entry(form)
        mae_entry.pack()

        tk.Label(form, text="Nacionalidade:").pack()
        nac_entry = tk.Entry(form)
        nac_entry.pack()

        tk.Label(form, text="Número de CPF").pack()
        email_entry = tk.Entry(form)
        email_entry.pack()

        def enviar_formulario():
            nome = nome_entry.get()
            data = data_entry.get()
            mae = mae_entry.get()
            nac = nac_entry.get()
            email = email_entry.get()
            print(f"Solicitação de CPF enviada para {nome} ({email})")
            messagebox.showinfo("Sucesso", "Solicitação de CPF enviada com sucesso!")

        tk.Button(form, text="Enviar", command=enviar_formulario).pack(pady=10)

    # ======= CHATBOT SIMPLES =======

    def process_chat(self):
        pergunta = self.entry.get()
        self.chatbox.config(state='normal')  # Habilita edição
        self.chatbox.insert(tk.END, f"Você: {pergunta}\n")
        resposta = self.responder(pergunta)
        self.chatbox.insert(tk.END, f"Bot: {resposta}\n")
        self.chatbox.config(state='disabled')  # Torna somente leitura novamente
        self.entry.delete(0, tk.END)


    # ======= RESPONDER PERGUNTAS [TESTE 1]=======
    def responder(self, pergunta):
        mensagens = PerguntasUsuario()
        if self.language == 'pt':
            pergunta = pergunta.lower()
            if any(mensagem in pergunta for mensagem in mensagens.get_mensagens_inicio()):
                return "Olá! Como posso lhe ajudar hoje?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_ajuda()):
                return "Claro! Como posso ajudar você?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_passaporte()):
                return "Para solicitar passaporte, clique no botão 'Solicitar Passaporte'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_cpf()):
                return "Para criar um CPF, clique no botão 'Criar CPF'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_registro()):
                return "O serviço de Registro Civil cobre nascimento, casamento e óbito."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_idioma()):
                return "Você pode trocar o idioma no menu suspenso acima."
            else:
                return "Desculpe, não entendi. Pode reformular?"
        
        elif self.language == "en":
            if any(mensagem in pergunta for mensagem in mensagens.get_mensagens_inicio()):
                return "Hello! How can I assist you today?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_ajuda()):
                return "Sure! How can I help you?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_passaporte()):
                return "To request a passport, click the 'Request Passport' button."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_cpf()):
                return "To create a CPF, click the 'Create CPF' button."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_registro()):
                return "The Civil Registration service covers birth, marriage, and death."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_idioma()):
                return "You can change the language in the dropdown menu above."
            else:
                return "Sorry, I didn't understand. Can you rephrase?"
        
        elif self.language == "es":
            if any(mensagem in pergunta for mensagem in mensagens.get_mensagens_inicio()):
                return "¡Hola! ¿Cómo puedo ayudarte hoy?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_ajuda()):
                return "¡Claro! ¿Cómo puedo ayudarte?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_passaporte()):
                return "Para solicitar un pasaporte, haga clic en el botón 'Solicitar Pasaporte'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_cpf()):
                return "Para crear un CPF, haga clic en el botón 'Crear CPF'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_registro()):
                return "El servicio de Registro Civil cubre nacimiento, matrimonio y defunción."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_idioma()):
                return "Puede cambiar el idioma en el menú desplegable de arriba."
            else:
                return "Lo siento, no entendí. ¿Puedes reformular?"
            
        elif self.language == "de":
            if any(mensagem in pergunta for mensagem in mensagens.get_mensagens_inicio()):
                return "Hallo! Wie kann ich Ihnen heute helfen?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_ajuda()):
                return "Natürlich! Wie kann ich Ihnen helfen?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_passaporte()):
                return "Um einen Pass zu beantragen, klicken Sie auf die Schaltfläche 'Pass beantragen'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_cpf()):
                return "Um eine CPF zu erstellen, klicken Sie auf die Schaltfläche 'CPF erstellen'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_registro()):
                return "Der Standesamtdienst umfasst Geburt, Ehe und Tod."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_idioma()):
                return "Sie können die Sprache im Dropdown-Menü oben ändern."
            else:
                return "Entschuldigung, ich habe es nicht verstanden. Können Sie umformulieren?"
        
        elif self.language == "it":
            if any(mensagem in pergunta for mensagem in mensagens.get_mensagens_inicio()):
                return "Ciao! Come posso aiutarti oggi?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_ajuda()):
                return "Certo! Come posso aiutarti?"
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_passaporte()):
                return "Per richiedere un passaporto, fai clic sul pulsante 'Richiedi Passaporto'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_cpf()):
                return "Per creare un CPF, fai clic sul pulsante 'Crea CPF'."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_registro()):
                return "Il servizio di Registrazione Civile copre nascita, matrimonio e morte."
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_idioma()):
                return "Puoi cambiare la lingua nel menu a discesa sopra."
            else:
                return "Mi dispiace, non ho capito. Puoi riformulare?"


    # ======= RESPONDER PERGUNTAS [TESTE 2]=======
    '''def responder(self, pergunta):
        if self.language == 'pt':
            pergunta = pergunta.lower()
            if "passaporte" in pergunta:
                return "Para solicitar passaporte, clique no botão 'Solicitar Passaporte'."
            elif "registro" in pergunta:
                return "O serviço de Registro Civil cobre nascimento, casamento e óbito."
            elif "cpf" in pergunta:
                return "Para criar um CPF, clique no botão 'Criar CPF'."
            elif "idioma" in pergunta or "traduzir" in pergunta:
                return "Você pode trocar o idioma no menu suspenso acima."
            elif "Oi" or "Olá" in pergunta:
                return "Como posso lhe ajudar?"
            else:
                return "Desculpe, não entendi. Pode reformular?"
            
        if self.language == "en":
            if "passport" in pergunta:
                return "To request a passport, click the 'Request Passport' button."
            elif "registration" in pergunta:
                return "The Civil Registration service covers birth, marriage, and death."
            elif "cpf" in pergunta:
                return "To create a CPF, click the 'Create CPF' button."
            elif "language" in pergunta or "translate" in pergunta:
                return "You can change the language in the dropdown menu above."
            elif "hi" or "hello" in pergunta:
                return "How can I assist you?"
            else:
                return "Sorry, I didn't understand. Can you rephrase?"
            
        if self.language == "es":
            if "pasaporte" in pergunta:
                return "Para solicitar un pasaporte, haga clic en el botón 'Solicitar Pasaporte'."
            elif "registro" in pergunta:
                return "El servicio de Registro Civil cubre nacimiento, matrimonio y defunción."
            elif "cpf" in pergunta:
                return "Para crear un CPF, haga clic en el botón 'Crear CPF'."
            elif "idioma" in pergunta or "traducir" in pergunta:
                return "Puede cambiar el idioma en el menú desplegable de arriba."
            elif "hola" in pergunta or "saludo" in pergunta:
                return "¿Cómo puedo ayudarte?"
            else:
                return "Lo siento, no entendí. ¿Puedes reformular?"
        
        if self.language == "de":
            if "pass" in pergunta:
                return "Um Pass zu beantragen, klicken Sie auf die Schaltfläche 'Pass beantragen'."
            elif "registrierung" in pergunta:
                return "Der Standesamtdienst umfasst Geburt, Ehe und Tod."
            elif "cpf" in pergunta:
                return "Um eine CPF zu erstellen, klicken Sie auf die Schaltfläche 'CPF erstellen'."
            elif "sprache" in pergunta or "übersetzen" in pergunta:
                return "Sie können die Sprache im Dropdown-Menü oben ändern."
            elif "hallo" in pergunta or "grüße" in pergunta:
                return "Wie kann ich Ihnen helfen?"
            else:
                return "Entschuldigung, ich habe es nicht verstanden. Können Sie umformulieren?"
        
        if self.language == "it":
            if "passaporto" in pergunta:
                return "Per richiedere un passaporto, fai clic sul pulsante 'Richiedi Passaporto'."
            elif "registrazione" in pergunta:
                return "Il servizio di Registrazione Civile copre nascita, matrimonio e morte."
            elif "cpf" in pergunta:
                return "Per creare un CPF, fai clic sul pulsante 'Crea CPF'."
            elif "lingua" in pergunta or "tradurre" in pergunta:
                return "Puoi cambiare la lingua nel menu a discesa sopra."
            elif "ciao" in pergunta or "saluto" in pergunta:
                return "Come posso aiutarti?"
            else:
                return "Mi dispiace, non ho capito. Puoi riformulare?"'''
                

    # ======= TRADUÇÃO DA INTERFACE =======

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

        textos = {
            self.label_title: "Bem-vindo ao Consulado",
            self.btn_passaporte: "Solicitar Passaporte",
            self.btn_registro: "Registro Civil",
            self.btn_cpf: "Criar CPF"
        }

        for widget, texto_original in textos.items():
            try:
                traducao = self.translator.translate(texto_original, src='pt', dest=self.language).text
                widget.config(text=traducao)
            except Exception as e:
                print(f"Erro na tradução: {e}")


# ======= EXECUÇÃO DO APP =======

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsuladoApp(root)
    root.mainloop()
