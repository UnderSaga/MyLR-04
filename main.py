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
    pass


def dublicate_2(d1):
    pass


if __name__ == '__main__':
    input_n()