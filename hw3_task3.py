def thesaurus(*args):
    result = {}
    for name in args:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


for k, v in thesaurus("Иван", "Мария", "Петр", "Илья", "Павел", "Дима", "Даша", "Друзь").items():
    print(f'"{k}": {v}', sep=':')
