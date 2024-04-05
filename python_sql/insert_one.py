import sqlite3
import random

nomes = [
    "João", "Maria", "José", "Ana", "Pedro", "Mariana", "Carlos", "Juliana", "Paulo", "Luciana",
    "Fernando", "Camila", "Antônio", "Amanda", "Luiz", "Isabela", "Rafael", "Beatriz", "Gustavo", "Natália",
    "Daniel", "Carolina", "Diego", "Roberta", "Felipe", "Patrícia", "Ricardo", "Larissa", "Eduardo", "Letícia",
    "Vinícius", "Vanessa", "Marcelo", "Tatiane", "Leandro", "Aline", "Rodrigo", "Fernanda", "Gabriel", "Carla",
    "André", "Laura", "Guilherme", "Bianca", "Renato", "Michelle", "Arthur", "Thaís", "Leonardo", "Natasha",
    "Raul", "Sabrina", "Jorge", "Jéssica", "Rafaela", "Douglas", "Luana", "César", "Daniela", "Bernardo",
    "Adriana", "Fábio", "Cristiane", "Ricardo", "Renata", "Fábio", "Renata", "Luiz", "Juliana", "Roberto",
    "Silvana", "Marcos", "Priscila", "Thiago", "Monique", "Alan", "Nathalia", "Caio", "Caroline", "Sérgio",
    "Érica", "Matheus", "Talita", "Alexandre", "Verônica", "Marcela", "Lívia", "Samuel", "Raquel", "Miguel",
    "Tainá", "Victor", "Bruna", "Lucas", "Cintia", "Anderson", "Simone", "Diego", "Júlia", "Wellington",
    "Denise"
]

conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()
for i in range(100):
    var = random.randint(1, 80)
    sql = f'insert into tb_cliente(cpf, nome, idade) values("{i}", "{nomes[i]}", {var})'
    cur.execute(sql)
    conexao.commit()
cur.close
conexao.close()
print("Fechou a  base de dados")