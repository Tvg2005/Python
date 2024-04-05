import sqlite3
database = 'livraria.db'
conexao = sqlite3.connect(database)
cur = conexao.cursor()
sql = '''create table if not exists tb_cliente(
    cpf text primary key,
    nome text not null,
    idade integer)'''
cur.execute(sql)
cur.close()
conexao.close()
print('fechou a base de dados')