# importando SQLite
import sqlite3 as lite

# CRUD
# -> Creaty = inserir / criar
# -> Ready = acessar / mostrar
# -> Update = atualizar /
# -> Delete = deletar / apagar

# criando a conexão com o bd
conexao = lite.connect("dados.db")

lista_cadastro = ['Juarez Santana',  'jssjr@gmail.com',
                  71987757575, "01/15/2023", 'Normal', 'consultar pessoalmente']


# função cadastrar
with conexao:
    cur = conexao.cursor()
    # comandos do SQL
    query = "INSERT INTO formulario (nome, email, telefone, data_consulta, situacao, observacao) VALUES (?, ?, ?, ?, ?, ?)"
    # comando para executar o query
    cur.execute(query, lista_cadastro)


# acessar informações
with conexao:
    cur = conexao.cursor()
    # * - sig tudo
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)


lista_atualizar = ["Júnior", 1]
# função atualizar
with conexao:
    cur = conexao.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query, lista_atualizar)


lista_deletar = [1]
# função deletar
with conexao:
    cur = conexao.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista_deletar)
