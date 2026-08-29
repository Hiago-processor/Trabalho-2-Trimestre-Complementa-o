import sqlite3

conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUTOS (
    PRODUTOS_ID INT PRIMARY KEY,
    NOME_PDT VARCHAR(150) NOT NULL,
    CATEGORIA VARCHAR(50) NOT NULL,
    MATERIAL VARCHAR(50) NOT NULL,
    VALOR DECIMAL(10, 2) NOT NULL,
    TAMANHO VARCHAR(50) NOT NULL
);
""")

produtos = [
    (1, 'Protetor de carregador', 'uso pessoal', 'PLA PREMIUM', 24.90, '8x2.2x1.8cm'),
]

cursor.executemany("""
INSERT OR IGNORE INTO PRODUTOS 
(PRODUTOS_ID, NOME_PDT, CATEGORIA, MATERIAL, VALOR, TAMANHO)
VALUES (?, ?, ?, ?, ?, ?);
""", produtos)

cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENTE (
    CLIENTE_ID INT PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    DATA DATE NOT NULL,
    EMAIL VARCHAR(100) UNIQUE NOT NULL,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    CEP VARCHAR(9) NOT NULL,
    TELEFONE VARCHAR(15) NOT NULL,
    ENDER VARCHAR(150) NOT NULL,
    NCASA INT NOT NULL,
    COMPLE VARCHAR(50),
    CITY VARCHAR(50) NOT NULL,
    UF CHAR(2) NOT NULL,
    OBS TEXT
);
""")

cliente = [
    (1, 'Pedro', '2015-03-10', 'pedro.balde@gmail.com', '111.526.426-19', '83702-050', '41 9666-1670', 'Rua Fernando Pinho de Azevedo', 49, 'casa preta', 'Araucária', 'PR', 'Cliente bom, educado, e bondoso'),
]


cursor.executemany("""
INSERT OR IGNORE INTO CLIENTE 
(CLIENTE_ID, NOME, DATA, EMAIL, CPF, CEP, TELEFONE, ENDER, NCASA, COMPLE, CITY, UF, OBS)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", cliente)


conexion.commit()

print("--- Clientes cadastrados no banco ---")
cursor.execute("SELECT CLIENTE_ID, NOME, EMAIL, CITY, UF FROM CLIENTE;")
clientes_cadastrados = cursor.fetchall()

for row in clientes_cadastrados:
    print(f"ID: {row[0]} | Nome: {row[1]} | E-mail: {row[2]} | Cidade: {row[3]}/{row[4]}")

conexion.close()
