import sqlite3

conexao = sqlite3.connect('AgendaDB.py')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'idade INTEGER'
               ')')
cursor.execute('INSERT INTO clientes(nome, idade)VALUES ("Marco",30)')
conexao.commit()
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)
cursor.close()
conexao.close()