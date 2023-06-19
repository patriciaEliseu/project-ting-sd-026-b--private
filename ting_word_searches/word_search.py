from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        lines_with_word = []

        for line_num, line in enumerate(
            file_data["linhas_do_arquivo"],
            start=1,
        ):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_num})

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": lines_with_word,
            }
            results.append(result)

    return results


def search_by_word(word, instance):
    return exists_word(word, instance)
