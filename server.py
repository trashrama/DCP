from xmlrpc.server import SimpleXMLRPCServer
import sqlite3
import os
from random import randint


def envia(tupla):
    print("Cliente enviou os dados!")
    if not os.path.exists('banco.db') or os.path.getsize('banco.db') < 1:
        bd = sqlite3.connect('banco.db')
        cursor = bd.cursor()
        cursor.execute('''
        CREATE TABLE ALUNOS (
        matricula integer primary key,
        nome varchar,
        nota double);
        ''')
        bd.commit()
        bd.close()

    bd = sqlite3.connect('banco.db')
    cursor = bd.cursor()

    try:
        cursor.execute("INSERT INTO ALUNOS VALUES (?, ?, ?)",
                       (tupla[0], tupla[1], tupla[2]))
    except sqlite3.IntegrityError as e:
        if ('UNIQUE constraint failed' in str(e)):
            print('Erro ao inserir valores: os valores já existem')

    cursor.execute(
        f"UPDATE ALUNOS SET nota = {randint(10, 100) / 10} WHERE matricula = {tupla[0]}")

    bd.commit()
    bd.close()


def main():
    server = SimpleXMLRPCServer(("localhost", 6969), allow_none=True)
    server.register_function(envia, 'envia')
    server.serve_forever()
    print("****** SERVIDOR INICIADO ******")


main()
