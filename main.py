'''
от себя:
- добавлено меню для циклического выбора задач, пока не введене "exit"
- проверка ввода пользователя на корректность
- к задачам со списками добавлены варианты генерации случайных списков
'''

from Less5_1 import fruitslist as exc1
from Less5_2 import excer as exs2
from Less5_3 import excer as exs3
from Less5_4 import do_exc as exs4

func = {
    1: exc1,
    2: exs2,
    3: exs3,
    4: exs4
}


def check_input(value, limit):
    if value == "exit":
        raise SystemExit("Надеюсь вам понравилось.")
    try:
        val = int(value)
        if val < 0 or val > limit:
            return check_input(input(f"Возможно только {limit} вариантов."), limit)
        else:
            return val
    except ValueError:
        print("Вы ввели не число")
        return check_input(input("Введите число:\r\n"), limit)


if __name__ == "__main__":
    while True:
        print("Варианты:", "1.Задача про фрукты", "2.Задача про выбор из списка", "3.Задача про выбор из списка 2",
              "4.Задача про число 13", "Для выхода наберите 'exit'", sep="\r\n")
        try:
            fu = check_input(input("Введите номер:\r\n"), len(func))
        except SystemExit as e:
            print(e)
            break
        if fu in [1, 2, 3]:
            print(f"Выбрана задача №{fu}.")
            fu2 = check_input(input('Использовать в задаче\r\n1.Сгенерировать список\r\n2.Заданый в условии список\r\n '), 2)
            func[int(fu)](fu2)
        if int(fu) == 4:
            func[int(fu)]()



