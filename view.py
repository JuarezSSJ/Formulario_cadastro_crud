# importando SQLite
import sqlite3 as lite

# CRUD
# -> Creaty = inserir / criar
# -> Ready = acessar / mostrar
# -> Update = atualizar /
# -> Delete = deletar / apagar

# criando a conexão com o bd
conexao = lite.connect("dados.db")


# função cadastrar
def cadastrar_info(i):
    with conexao:
        cur = conexao.cursor()
        # comandos do SQL
        query = "INSERT INTO formulario (nome, email, telefone, data_consulta, situacao, observacao) VALUES (?, ?, ?, ?, ?, ?)"
        # comando para executar o query
        cur.execute(query, i)



# acessar informações
def apresentar_info():
    lista_apresentar = []
    with conexao:
        cur = conexao.cursor()
        # * - sig tudo
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        #corre toda a lista da info e mandar para a lista_apresentar
        for i in info:
            lista_apresentar.append(i)
    return lista_apresentar



# função atualizar
def atualizar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, data_consulta=?, situacao=?, observacao=? WHERE id=?"
        cur.execute(query, i)



# função deletar
def deletar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)


# acessar informações para analisar
def analisar_info():
    lista_coluna_analisar = []
    with conexao:
        cur = conexao.cursor()
        # * - sig tudo
        query = "SELECT COUNT (DISTINCT situacao) FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        #corre toda a lista da info e mandar para a lista_apresentar
        for i in info:
            lista_coluna_analisar.append(i)
    return lista_coluna_analisar