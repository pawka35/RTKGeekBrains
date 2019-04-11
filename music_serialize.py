'''
Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''

import json
import pickle


def __write_pickle(filename, obj):
    
    try:    
        with open(filename, 'wb') as filePickle:
            pickle.dump(obj, filePickle)
    except :
        return f'Создание файла {filename} не удалось'


def __write_json(filename, obj):
    try:
        with open(filename, 'w', encoding='utf-8') as fileJson:
            json.dump(obj, fileJson)
    except:
        return f'Создание файла {filename} не удалось'


def __append_file(filename, obj):
    with open(filename, 'r', encoding='utf-8') as file:
        file_data = json.load(file)
    file_data.append(obj)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(file_data, file)


def write_file(filename, obj, append=False):
    file_type = filename.split('.')[1]
    if file_type == 'json':
        if append:
            return __append_file(filename,obj)
        else:
            return __write_json(filename, obj)
    elif file_type == 'pickle':
        return __write_pickle(filename, obj)
    else:
        raise ValueError('Не верно указано расширение для файла')


def write_to_console(obj, method):
    if method == 'json':
        return json.dumps(obj)
    else:
        return pickle.dumps(obj)
