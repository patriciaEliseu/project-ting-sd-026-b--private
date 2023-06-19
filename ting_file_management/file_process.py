import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instancia):
    for i in range(len(instancia)):
        r = instancia.search(i)
        if r["nome_do_arquivo"] == path_file:
            return
    data = txt_importer(path_file)
    dict_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instancia.enqueue(dict_return)
    print(dict_return)


def remove(instancia):
    if not len(instancia):
        print("Não há elementos")
    return

    removed = instancia.dequeue()
    print(f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instancia, position):
    try:
        print(instancia.search(position))
    except Exception:
        print("Posição inválida", file=sys.stderr)
