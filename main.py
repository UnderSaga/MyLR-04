from os import *


def input_n():
    n = input('Введите путь к папке: ')
    if path.exists(n):
        return n
    else:
        return input_n()


def dictionary(n):
    d1 = {}
    for i in listdir(n):
        current_path = path.join(n, i)
        if path.isdir(current_path):
            d1.update(dictionary(current_path))
        else:
            d1[current_path] = path.getsize(current_path)
    return d1


def dublicate(d1):
    dubl = {}
    for way, size in d1.items():
        name1 = str(path.basename(way)) + '_' + str(size)
        if name1 in dubl.keys():
            dubl.get(name1).append(way)
        else:
            dubl[name1] = [way]
    d1.clear()
    for name1, filesize in dubl.items():
        if len(filesize) > 1:
            d1[name1] = filesize
    return d1


def dublicate_2(d1):
    if len(d1) == 0:
        print('Дубликатов нет')
    else:
        for filename, ways in d1.items():
            size = path.getsize(ways[0])
            print(size)
            for x in ways:
                print(x)
            print()



if __name__ == '__main__':
    input_n()
