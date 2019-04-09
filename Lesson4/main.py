'''
3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций. 
Вызовите каждую функцию в main.py и проверьте, что все работает как надо.

От себя:
- зацикливание алгоритма, пока пользователь не выберет выход
- организация меню выбора, какую функцию вызываем
- проверки введенных значений (реализовано в отдельном модуле check_module.py)
- использование словаря для аналога некого switch-case алгоритма
'''
from exc4_1 import make_directories as makedir
from exc4_1 import del_directories as deldir
import exc4_2 as element_choise
from check_module import check_value


functions = {
    1: makedir,
    2: deldir,
    3: element_choise.manual_enter,
    4: element_choise.auto_enter
    }

if __name__=='__main__':
    while True:
        print("Выберите действие:", "1.Создать папки.","2.Удалить папки.","3.Задача 2 с ручным вводом списка.",\
            "4.Задача 2 с автогенериуемым списком.",\
            sep="\r\n")
        choise = check_value(input(),4,"entervariant")
        func = functions[choise]
        func()
        cont = check_value(input('Хотите продолжить?(y/n):'),None,"continue")
        if not cont:
            break

