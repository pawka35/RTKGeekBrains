'''
1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py). 
В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код. 
Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

От себя:
- обработка ошибки создания папки, если уже существует
- вывод каталогов до и после создания\удаления
'''

import os,sys


def make_directories():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),f'dir_{i}')
        try:
            os.mkdir(new_path)
        except FileExistsError:
            print(f'Папка {new_path} уже существует. Создаваться не будет.')
            
    print("Процедура создания папок завершена.","Текущий список каталогов директории:",sep='\r\n')
    for p in os.listdir():
        print(p)

def del_directories():
    for p in os.listdir():
        if 'dir_' in p:
            os.removedirs(p)
    print("Удаление папок завершено")
    for p in os.listdir():
        print(p)

if __name__=='__main__':
    make_directories()
    del_directories()

