import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('database.db')

# Criando um cursor
cursor = conn.cursor()

# Criando a tabela 'configuracoes'
cursor.execute('''
CREATE TABLE IF NOT EXISTS configuracoes (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    tema TEXT,
    fonte TEXT,
    tamanho_fonte INTEGER,
    cor_fonte TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);
''')

# Salvando as alterações
conn.commit()

# Fechando a conexão
conn.close()

#def deletar_tabela_configuracoes():
    # Conectar-se ao banco de dados
#    conn = sqlite3.connect('database.db')
#    cursor = conn.cursor()

    # Deletar a tabela "configuracoes"
#    cursor.execute("DROP TABLE IF EXISTS configuracoes")

    # Salvar as alterações e fechar a conexão com o banco de dados
#    conn.commit()
#    conn.close()
