'''
2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

От себя:
- 2 варианта генерации списка: вручную и случайным образом
- проверки введенных значений (реализовано в отдельном модуле check_module.py)
- возможны случаи обнуления списка (почему при list.clear() list становится None? довольно неочивидная вещь)

'''
import random
from check_module import check_value

def list_generator():
    list = []
    for _ in range(5, random.randrange(10,20)):
        list.append(random.randint(1,100))
    return list

def return_element(list):
    if list is None or len(list)==0:
        return None
    else: 
        return random.choice(list)



def make_list():
    elements_count = check_value(input("Введите количество элементов в списке: "),None,"entercounts")
    list=[]
    for i in range(0,elements_count):
        list.append(check_value(input(f'Введите элемент №{i+1}: '),i,"enternumbers"))
    return list

def make_choise(list):
    print(f'Первоначально сгенерированный список: \r\n{list}')
    choise = random.randint(0,2)
    if choise == 0:
        print("Выпал вариант при котором исходный список не изменяется")
        element = return_element(list)
        print(f'Функция вернула элемент: {element} (на {list.index(element)+1} месте в списке).')
    elif choise == 1:
        print("Выпал вариант с очисткой спиcка функцией clear.")
        list.clear()
        print(f'Функция вернула элемент: {return_element(list)}')
    elif choise == 2:
        print("Выпал вариант с очисткой спиcка присвоением ссылки на пустой список")
        list = []
        print(f'Функция вернула элемент: {return_element(list)}')

def manual_enter():
    make_choise(make_list())

def auto_enter():
    make_choise(list_generator())

if __name__=='__main__':
    print("Вариант 1 (ручной ввод списка): ")
    list = make_list();
    make_choise(list)
    print("=|"*50)
    print("Вариант 2 (автогенерация списка): ")
    list = list_generator()
    make_choise(list)

