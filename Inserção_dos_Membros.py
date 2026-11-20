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

cursor.close()
connection.close()