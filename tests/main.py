import tkinter as tk
import requests

def traduzir():
    texto = entrada.get()
    if texto:
        url = "https://translate.argosopentech.com/translate"
        dados = {
            "q": texto,
            "source": "auto",
            "target": "pt",
            "format": "text"
        }
        resposta = requests.post(url, json=dados)
        if resposta.ok:
            traducao = resposta.json()["translatedText"]
            saida_var.set(traducao)
        else:
            saida_var.set("Erro na tradução: " + resposta.text)

janela = tk.Tk()
janela.title("Tradutor com LibreTranslate")

tk.Label(janela, text="Texto para traduzir:").pack(pady=5)

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

tk.Button(janela, text="Traduzir", command=traduzir).pack(pady=10)

saida_var = tk.StringVar()
tk.Label(janela, textvariable=saida_var, wraplength=400, fg="blue").pack(pady=10)

janela.mainloop()
