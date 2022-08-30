import sqlite3

class AgendaDB:
    def _init_(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome = ?, telefone = ? WHERE id = ?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id = ?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT nome, telefone FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if  '__name__' == '_main_':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Pedro', '47992628664' , 'josé','4899225566')
    agenda.listar('Pedro', '47992628664' , 'josé','4899225566')