#DROP DA TABELA CANDIDATOS DENTRO DO BANCO DATABA
#import sqlite3
#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()
 # Verifica se a tabela "candidatos" existe
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='candidatos'")
#table_exists = cursor.fetchone()
#if table_exists:
     # Executa o comando DROP TABLE para remover a tabela "candidatos"
#    cursor.execute("DROP TABLE candidatos")
#    print("Tabela 'candidatos' removida com sucesso.")
#else:
#    print("A tabela 'candidatos' não existe.")
#conn.commit()
#conn.close()

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE candidatos (
    id INTeger PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    sexo VARCHAR(20) NOT NULL,
    estado_civil VARCHAR(20) NOT NULL,
    quantidade_filhos INT NOT NULL,
    idade_filho_1 INT NOT NULL,
    escolaridade VARCHAR(50) NOT NULL,
    area_formacao VARCHAR(100) NOT NULL,
    entidade VARCHAR(100) NOT NULL,
    logradouro VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(100),
    filial VARCHAR(10) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    admissao DATE NOT NULL,
    praca VARCHAR(100) NOT NULL,
    vale_transporte VARCHAR(3),
    entrevistador VARCHAR(100) NOT NULL,
    data_entrevista DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    grau_anotacao VARCHAR(20),
    anotacao TEXT )
''')
conn.commit()
conn.close()
