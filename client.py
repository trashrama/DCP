import ezodf
import xmlrpc.client


def tratamento():
    lista = []
    listaTuplas = []

    f = ezodf.opendoc('bd.ods')
    planilha = f.sheets[0]

    colunas = planilha.columns()

    for linha in zip(*colunas):
        valores = [celula.value for celula in linha]
        lista.append(valores)

    lista.pop(0)

    for l in lista:
        matriculaInt = int(l[0])
        listaTuplas.append((matriculaInt,) + tuple(l[1:]))
        # matriculaInt foi convertido pra uma tupla unária que se fundiu com o resto da outra parte da lista
        # e que agora, é por si só uma tupla de novo.
    return listaTuplas


def main():
    client = xmlrpc.client.ServerProxy(
        "http://localhost:6969/", allow_none=True)

    for tupla in tratamento():
        client.envia(tupla)


main()
