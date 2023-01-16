# importando SQLite
import sqlite3 as lite

# Criando conexão
conexao = lite.connect("dados.db")

# Criando tabela
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, data_consulta DATE, situacao TEXT, observacao TEXT)")
    #comando para deletar a tabela
    #cur.execute("DROP TABLE formulario")