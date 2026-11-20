import mysql.connector
import os

connection = mysql.connector.connect(
    host="200.235.131.219",
    user="grupo2",
    password="K3Ab6Uw9",
    database="grupo2"
)

cursor = connection.cursor()

membros = [
    (120565, "Bruno Alexander Pinto Sette"),
    (120552, "João Pedro Nunes Monteiro Silva"),
    (120568, "Eduardo Magesti Santiago"),
    (120582, "Paulo Henrique de Souza Castro"),
    (120558, "Thales Rodrigues Neves")
]

cursor.executemany("""
    INSERT INTO MEMBROS_DO_GRUPO (matricula, nome)
    VALUES (%s, %s);
""", membros)

connection.commit()

cursor.execute("SHOW TABLES")
tabelas = cursor.fetchall()

print("\n========== TABELAS DO BANCO ==========")

for tabela in tabelas:
    nome_tabela = tabela[0]

    print(f"\n{'=' * 50}")
    print(f"TABELA: {nome_tabela}")
    print("=" * 50)

    # Consultar os registros da tabela
    cursor.execute(f"SELECT * FROM `{nome_tabela}`")

    # Obter os nomes das colunas
    colunas = [desc[0] for desc in cursor.description]

    print("Colunas:", colunas)

    # Obter todos os registros
    registros = cursor.fetchall()

    if registros:
        for registro in registros:
            print(registro)
    else:
        print("Tabela vazia.")

    print(f"\nTotal de registros: {len(registros)}")


cursor.close()
connection.close()