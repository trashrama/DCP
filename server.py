from xmlrpc.server import SimpleXMLRPCServer
import sqlite3
import os


def envia(tupla):
    bd = sqlite3.connect('banco.db')
    cursor = bd.cursor()

    if not os.path.exists('banco.db') or os.path.getsize('banco.db') < 1:
        cursor.execute('''
        CREATE TABLE ALUNOS (
        matricula integer primary key,
        nome varchar,
        nota double);
        ''')

    try:
        cursor.execute("INSERT INTO ALUNOS VALUES (?, ?, ?)",
                       (tupla[0], tupla[1], tupla[2]))
    except sqlite3.IntegrityError as e:
        if ('UNIQUE constraint failed' in e):
            print('Erro ao inserir valores: os valores já existem')
    cursor.execute("UPDATE ALUNOS SET nota = 8 WHERE matricula = 1324")

    bd.commit()
    bd.close()


def main():
    server = SimpleXMLRPCServer(("localhost", 6969), allow_none=True)
    server.register_function(envia, 'envia')
    server.serve_forever()


main()
