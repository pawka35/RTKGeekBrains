'''
 Создать модуль music_deserialize.py.
 В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
 Получить объект — словарь из предыдущего задания.
'''

import json
import pickle


def __read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as filejson:
            return json.load(filejson)
    except FileNotFoundError:
       return f'Файл {filename} не найден.'
    except:
        raise ValueError(f'Чтение файла {filename} не удалось.')


def __read_pickle(filename):
    try:
        with open(filename, 'rb') as filePickle:
            return pickle.load(filePickle)
    except FileNotFoundError as e:
       return f'Файл {filename} не найден.'
    except:
        raise ValueError(f'Чтение файла {filename} не удалось.')


def readfile(filename):
    filetype = filename.split('.')[1]
    if filetype == 'json':
        return __read_json(filename)
    elif filetype == 'pickle':
        return __read_pickle(filename)
    else:
        raise ValueError('Не верно указано расширение для файла')


def read_to_console(obj, method):
    if method == 'json':
        return json.loads(obj)
    else:
        return pickle.loads(obj)
