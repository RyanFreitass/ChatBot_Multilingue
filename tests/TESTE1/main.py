import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
from mensagens_teste.perguntas import PerguntasUsuario
from Expressoes_regulares.validar import Validacao
from database import criar_tabelas, inserir_passaporte, inserir_registro, inserir_cpf
from Expressoes_regulares.gerador_cpf import Gerador
import sqlite3
import os


class ConsuladoApp:
    def __init__(self, root):
        criar_tabelas()
        self.root = root
        self.root.title("Atendimento Consular Inteligente")
        import os
        self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "img", "icon.ico")) #Logo do Sistema
        self.translator = Translator()
        self.language = 'pt'  # default language

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

        self.btn_relacao = tk.Button(self.root, text="Relação de Solicitações", command=self.abrir_relacao)
        self.btn_relacao.pack(pady=5)

        self.root.configure(bg='#f5f5dc') # backgroundcolor

        self.language_selector = ttk.Combobox(
            self.root,
            values=["Português", "Inglês", "Espanhol", "Alemão", "Italiano"]
        )
        self.language_selector.current(0)
        self.language_selector.pack(pady=5)
        self.language_selector.bind("<<ComboboxSelected>>", self.translate_interface)
        self.language_selector.config(state='readonly')


        # Chatbot simples
        self.chatbox = tk.Text(self.root, height=12, width=70, bg='gray', fg='black')
        self.chatbox.pack(pady=10)
        self.chatbox.config(state='disabled')

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5)  # Centraliza por padrão

        self.entry = tk.Entry(input_frame, width=45, bg='gray', fg='black', insertbackground='black')
        self.entry.pack(side=tk.LEFT, padx=5)
        self.send_btn = tk.Button(input_frame, text="Enviar", command=self.process_chat)
        self.entry.bind("<Return>", lambda event: self.process_chat())
        self.send_btn.pack(side=tk.LEFT, padx=5)

    # ======= FORMULÁRIOS =======
    
    def acao_passaporte(self):
        form = tk.Toplevel(self.root)
        form.title(self.traduzir("Formulário de Solicitação de Passaporte"))

        tk.Label(form, text=self.traduzir("Nome Completo:")).pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text=self.traduzir("Data de Nascimento (DD/MM/AAAA):")).pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text=self.traduzir("Número de Identidade (RG):")).pack()
        rg_entry = tk.Entry(form)
        rg_entry.pack()

        tk.Label(form, text=self.traduzir("E-mail para contato:")).pack()
        email_entry = tk.Entry(form)
        email_entry.pack()

        def enviar_formulario():
            nome = nome_entry.get()
            data = data_entry.get()
            rg = rg_entry.get()
            email = email_entry.get()

            if not nome or not data or not rg or not email:
                messagebox.showwarning(self.traduzir("Dados Incompletos"), self.traduzir("Preencha todos os campos"))
                return
            
            if Validacao.validar_data(data) != "Data Válida":
                messagebox.showerror(self.traduzir("Erro"), self.traduzir("Data inválida. Formato correto: DD/MM/AAAA"))
                return
            
            if not Validacao.validar_email(email):
                messagebox.showerror(self.traduzir("Erro"), self.traduzir("E-mail inválido. Verifique o formato e tente novamente."))
                return
            
            if not Validacao.validacao_rg(rg):
                messagebox.showerror(self.traduzir("Erro"), self.traduzir("RG inválido. Verifique o formato e tente novamente."))
                return

            inserir_passaporte(nome, data, rg, email)
            print(self.traduzir(f"Solicitação de passaporte enviada para {nome} - {email}"))
            messagebox.showinfo(self.traduzir("Sucesso"), self.traduzir("Formulário enviado com sucesso!"))

        tk.Button(form, text=self.traduzir("Enviar"), command=enviar_formulario).pack(pady=10)

    def acao_registro(self):
        form = tk.Toplevel(self.root)
        form.title(self.traduzir("Formulário de Registro Civil"))

        tk.Label(form, text=self.traduzir("Tipo de Registro:")).pack()
        tipo_var = tk.StringVar()
        tipo_combobox = ttk.Combobox(form, textvariable=tipo_var, values=["Nascimento", "Casamento", "Óbito"])
        tipo_combobox.pack()
        tipo_combobox.config(state='readonly')

        tk.Label(form, text=self.traduzir("Nome Completo:")).pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text=self.traduzir("Data do Evento (DD/MM/AAAA):")).pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text=self.traduzir("Local do Evento:")).pack()
        local_entry = tk.Entry(form)
        local_entry.pack()

        tk.Label(form, text=self.traduzir("Nome dos Pais (se aplicável):")).pack()
        pais_entry = tk.Entry(form)
        pais_entry.pack()

        def enviar_formulario():
            tipo = tipo_var.get()
            nome = nome_entry.get()
            data = data_entry.get()
            local = local_entry.get()
            pais = pais_entry.get()

            if not tipo or not nome or not data or not local or not pais:
                messagebox.showwarning(self.traduzir("Dados Incompletos"), self.traduzir("Preencha todos os campos"))
                return
            
            if Validacao.validar_data(data) != "Data Válida":
                messagebox.showerror(self.traduzir("Erro"), self.traduzir("Data inválida. Formato correto: DD/MM/AAAA"))
                return
            
            inserir_registro(tipo, nome, data, local, pais)
            print(self.traduzir(f"Solicitação de registro civil para {nome} ({tipo})"))
            print(f"Registro de {tipo} para {nome} enviado.")
            messagebox.showinfo(self.traduzir("Sucesso"), self.traduzir(f"Formulário de {tipo} enviado com sucesso!"))

        tk.Button(form, text=self.traduzir("Enviar"), command=enviar_formulario).pack(pady=10)
    
    def acao_cpf(self):
        form = tk.Toplevel(self.root)
        form.title(self.traduzir("Formulário de Solicitação de CPF"))

        tk.Label(form, text=self.traduzir("Nome Completo:")).pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text=self.traduzir("Data de Nascimento (DD/MM/AAAA):")).pack()
        data_entry = tk.Entry(form)
        data_entry.pack()

        tk.Label(form, text=self.traduzir("Nome da Mãe:")).pack()
        mae_entry = tk.Entry(form)
        mae_entry.pack()

        tk.Label(form, text=self.traduzir("Nacionalidade:")).pack()
        nac_entry = tk.Entry(form)
        nac_entry.pack()

        tk.Label(form, text=self.traduzir("Novo CPF:")).pack()
        cpf_var = tk.StringVar()
        cpf_entry = tk.Entry(form, textvariable=cpf_var, state='readonly')
        cpf_entry.pack()

        def gerar_cpf():
            gerador = Gerador()
            novo_cpf = gerador.generate_cpf()
            cpf_var.set(novo_cpf)
            btn_gerar_cpf.config(state='disabled')  # Desabilita o botão após gerar

        btn_gerar_cpf = tk.Button(form, text=self.traduzir("Gerar CPF"), command=gerar_cpf)
        btn_gerar_cpf.pack(pady=5)

        def enviar_formulario():
            nome = nome_entry.get()
            data = data_entry.get()
            mae = mae_entry.get()
            nac = nac_entry.get()
            cpf = cpf_var.get()
            if not nome or not data or not mae or not nac or not cpf:
                messagebox.showwarning(self.traduzir("Dados Incompletos"), self.traduzir("Preencha todos os campos"))
                return
            inserir_cpf(nome, data, mae, nac, cpf)
            print(self.traduzir(f"Solicitação de CPF enviada para {nome} ({cpf})"))
            messagebox.showinfo(self.traduzir("Sucesso"), self.traduzir("Solicitação de CPF enviada com sucesso!"))

        def enviar_formulario():
            nome = nome_entry.get()
            data = data_entry.get()
            mae = mae_entry.get()
            nac = nac_entry.get()
            cpf = cpf_var.get()
            if not nome or not data or not mae or not nac or not cpf:
                messagebox.showwarning(self.traduzir("Dados Incompletos"), self.traduzir("Preencha todos os campos"))
                return
            inserir_cpf(nome, data, mae, nac, cpf)
            print(self.traduzir(f"Solicitação de CPF enviada para {nome} ({cpf})"))
            messagebox.showinfo(self.traduzir("Sucesso"), self.traduzir("Solicitação de CPF enviada com sucesso!"))

        tk.Button(form, text=self.traduzir("Enviar"), command=enviar_formulario).pack(pady=10)

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
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_abrir_relacoes()):
                return "Para abrir relações, clique no botão 'Relação de Solicitações'."
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
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_abrir_relacoes()):
                return "To open relations, click the 'Relation Requests' button."
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
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_abrir_relacoes()):
                return "Para abrir relaciones, haga clic en el botón 'Relación de Solicitudes'."
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
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_abrir_relacoes()):
                return "Um Beziehungen zu öffnen, klicken Sie auf die Schaltfläche 'Beziehungsanfragen'."
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
            elif any(mensagem in pergunta for mensagem in mensagens.get_mensagens_abrir_relacoes()):
                return "Per aprire relazioni, fai clic sul pulsante 'Relazione di Richieste'."
            else:
                return "Mi dispiace, non ho capito. Puoi riformulare?"

    # ======= TRADUÇÃO DA INTERFACE =======
    def traduzir(self, texto):
        if self.language == "pt":
            return texto
        try:
            return self.translator.translate(texto, src='pt', dest=self.language).text
        except Exception as e:
            print(f"Erro na tradução: {e}")
            return texto


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
    
    def abrir_relacao(self):
        conn = sqlite3.connect('consulado.db')
        relacao_win = tk.Toplevel(self.root)
        relacao_win.title(self.traduzir("Relação de Solicitações"))

        notebook = ttk.Notebook(relacao_win)
        notebook.pack(fill=tk.BOTH, expand=True)

        # CPF
        frame_cpf = ttk.Frame(notebook)
        notebook.add(frame_cpf, text="CPF")
        tree_cpf = ttk.Treeview(frame_cpf, columns=("cpf", "nome", "data_nasc", "mae", "nac"), show="headings")
        for col, txt in zip(("cpf", "nome", "data_nasc", "mae", "nac"),
                            ["CPF", "Nome", "Data de Nascimento", "Nome da Mãe", "Nacionalidade"]):
            tree_cpf.heading(col, text=txt)
            tree_cpf.column(col, width=120)
        tree_cpf.pack(fill=tk.BOTH, expand=True)
        cursor = conn.cursor()
        cursor.execute("SELECT cpf_numero, nome, data_nascimento, mae, nacionalidade FROM cpf")
        for row in cursor.fetchall():
            tree_cpf.insert("", tk.END, values=row)

        def deletar_cpf():
            selected = tree_cpf.selection()
            if not selected:
                messagebox.showwarning("Atenção", "Selecione um cadastro para deletar.")
                return
            item = tree_cpf.item(selected[0])
            cpf_numero = item['values'][0]
            cursor.execute("DELETE FROM cpf WHERE cpf_numero = ?", (cpf_numero,))
            conn.commit()
            tree_cpf.delete(selected[0])
            messagebox.showinfo("Sucesso", "Cadastro de CPF deletado.")

        btn_del_cpf = tk.Button(frame_cpf, text="Deletar Selecionado", command=deletar_cpf)
        btn_del_cpf.pack(pady=5)

        # Passaporte
        frame_pass = ttk.Frame(notebook)
        notebook.add(frame_pass, text="Passaporte")
        tree_pass = ttk.Treeview(frame_pass, columns=("nome", "data_nasc", "rg", "email"), show="headings")
        for col, txt in zip(("nome", "data_nasc", "rg", "email"),
                            ["Nome", "Data de Nascimento", "RG", "E-mail"]):
            tree_pass.heading(col, text=txt)
            tree_pass.column(col, width=120)
        tree_pass.pack(fill=tk.BOTH, expand=True)
        cursor.execute("SELECT nome, data_nascimento, rg, email FROM passaporte")
        for row in cursor.fetchall():
            tree_pass.insert("", tk.END, values=row)

        def deletar_passaporte():
            selected = tree_pass.selection()
            if not selected:
                messagebox.showwarning("Atenção", "Selecione um cadastro para deletar.")
                return
            item = tree_pass.item(selected[0])
            rg = item['values'][2]
            cursor.execute("DELETE FROM passaporte WHERE rg = ?", (rg,))
            conn.commit()
            tree_pass.delete(selected[0])
            messagebox.showinfo("Sucesso", "Cadastro de Passaporte deletado.")

        btn_del_pass = tk.Button(frame_pass, text="Deletar Selecionado", command=deletar_passaporte)
        btn_del_pass.pack(pady=5)

        # Registro Civil
        frame_reg = ttk.Frame(notebook)
        notebook.add(frame_reg, text="Registro Civil")
        tree_reg = ttk.Treeview(frame_reg, columns=("tipo", "nome", "data", "local", "pais"), show="headings")
        for col, txt in zip(("tipo", "nome", "data", "local", "pais"),
                            ["Tipo", "Nome", "Data", "Local", "Pais"]):
            tree_reg.heading(col, text=txt)
            tree_reg.column(col, width=120)
        tree_reg.pack(fill=tk.BOTH, expand=True)
        cursor.execute("SELECT tipo, nome, data_evento, local_evento, pais FROM registro_civil")
        for row in cursor.fetchall():
            tree_reg.insert("", tk.END, values=row)

        def deletar_registro():
            selected = tree_reg.selection()
            if not selected:
                messagebox.showwarning("Atenção", "Selecione um cadastro para deletar.")
                return
            item = tree_reg.item(selected[0])
            nome = item['values'][1]
            data = item['values'][2]
            cursor.execute("DELETE FROM registro_civil WHERE nome = ? AND data_evento = ?", (nome, data))
            conn.commit()
            tree_reg.delete(selected[0])
            messagebox.showinfo("Sucesso", "Cadastro de Registro Civil deletado.")

        btn_del_reg = tk.Button(frame_reg, text="Deletar Selecionado", command=deletar_registro)
        btn_del_reg.pack(pady=5)

    
        relacao_win.protocol("WM_DELETE_WINDOW", lambda: (conn.close(), relacao_win.destroy()))


# ======= EXECUÇÃO DO APP =======

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsuladoApp(root)
    root.mainloop()