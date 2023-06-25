import sqlite3

# Conectar ao banco de dados (se o arquivo não existir, ele será criado)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar a tabela "conversas" com as colunas necessárias
cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        mensagem TEXT NOT NULL,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()
