import sqlite3

def criar_tabelas():
    conn = sqlite3.connect("consulado.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS passaporte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_nascimento TEXT,
            rg TEXT,
            email TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS registro_civil (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            nome TEXT,
            data_evento TEXT,
            local_evento TEXT,
            pais TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS cpf (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_nascimento TEXT,
            mae TEXT,
            nacionalidade TEXT,
            cpf_numero TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_passaporte(nome, data_nascimento, rg, email):
    conn = sqlite3.connect("consulado.db")
    c = conn.cursor()
    c.execute("INSERT INTO passaporte (nome, data_nascimento, rg, email) VALUES (?, ?, ?, ?)",
              (nome, data_nascimento, rg, email))
    conn.commit()
    conn.close()

def inserir_registro(tipo, nome, data_evento, local_evento, pais):
    conn = sqlite3.connect("consulado.db")
    c = conn.cursor()
    c.execute("INSERT INTO registro_civil (tipo, nome, data_evento, local_evento, pais) VALUES (?, ?, ?, ?, ?)",
              (tipo, nome, data_evento, local_evento, pais))
    conn.commit()
    conn.close()

def inserir_cpf(nome, data_nascimento, mae, nacionalidade, cpf_numero):
    conn = sqlite3.connect("consulado.db")
    c = conn.cursor()
    c.execute("INSERT INTO cpf (nome, data_nascimento, mae, nacionalidade, cpf_numero) VALUES (?, ?, ?, ?, ?)",
              (nome, data_nascimento, mae, nacionalidade, cpf_numero))
    conn.commit()
    conn.close()