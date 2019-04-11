'''
от себя:
- данный модуль объединяем 3 модуля в единую программу (2 из задания, 1 - добавленный)
- реализовано меню с выбором вызываемых функций
- проверка на существование файла
- реализована возможность дозаписи информации в файл json
- попытался реализовать нечто не подобии инкапсуляции путем импорта только основных(входных) методов, а внутри
модулей уже возможны различные варианты и возвращаемые результаты
- возможно не все так красиво, как хотелось, но хватило времени на все задумки :(
'''

import os
from music_serialize import write_file
from music_serialize import write_to_console
from music_deserialize import read_to_console
from music_deserialize import readfile

from addtojson import addtojson

my_favourite_group = [{
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
{'name': 'Шапито', 'year': 2014}]}]


def check_ext_of_file(filename):
     if os.path.exists(filename):
         return True
     else:
         return False


def write_main(append=False):
    while True:
        filename = input('Введите имя записанного файла(либо ентер для выхода): ')
        exist = check_ext_of_file(filename)
        if not exist and not append: #если не существует и не дозаписываем
            break
        elif exist and not append: #если существует и не дозаписываем
            agree=input(f'Файл с именем {filename} уже существует.Перезаписать?\r\n \("y" - перезапись; "n" - отменить действие):\r\n')
            if agree == "n":
                break
        elif not exist and append: # если не существует, но надо дозаписать
            print("Такого файла не существует, нельзя в него дозаписать")
        elif exist and append:
            break
    if not append:
        try:
            write_file(filename, my_favourite_group)
        except ValueError as e:
            print(e)
            write_main(append)
    else:
        data = addtojson()
        write_file(filename, data, append)


def read_main():
    while True:
        filename = input('Введите имя файла для чтения (либо ентер для выхода): ')
        if filename == "":
            break
        if not os.path.exists(filename):
            print('Такого файла не существует')
        else:
            return readfile(filename)


if __name__ == '__main__':
    while True:
        chs = int(input('Вариант:\r\n1.Сериализовать через json и вывести в консоль\r\n'\
        '2.Сериализовать через pickle и вывести в консоль\r\n' \
        '3.Записать в файл\r\n' \
        '4.Дозаписать в файл json\r\n' \
        '5.Прочитать из файла\r\n'))

        if chs == 1:
            obj = write_to_console(my_favourite_group,'pickle')
            print("Сериализованный pickle:", obj, type(obj), sep='\r\n')
            print("Десериализованный pickle:", read_to_console(obj, 'pickle'), type(read_to_console(obj, 'pickle')), sep='\r\n')
        elif chs == 2:
            obj = write_to_console(my_favourite_group, 'json')
            print("Сериализованный json:", obj, type(obj), sep='\r\n')
            print("Десериализованный json:", read_to_console(obj, 'json'), type(read_to_console(obj,'json')), sep='\r\n')
        elif chs == 3:
            write_main()
        elif chs == 4:
            write_main(True)
        elif chs == 5:
            print(read_main())
        else:
            print('Нет такого варианта')
        cancel = input('Закончили? ("y"): ')
        if cancel == 'y':
            break
