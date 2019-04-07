'''
1.  Создайте функцию, принимающую на вход имя, возраст и город проживания
#человека.
Функция должна возвращать строку вида «Василий, 21 год(а),проживает в городе
Москва»

От себя:
- проверка корректности ввода
- имена собственные обязательно преобразуем, чтобы начинались с большой буквы
- вывод 2 способами: через передачу списка параметров, через передачу именованных параметров
- программа зациклина, пока пользователь явно ен выберет вариант выхода
'''

def fuc(**kwargs):
   return f'{name}, {age} год(а), проживает в городе {city}'

def fuc2(*args):
    return f'{args[0]}, {args[1]} год(а), проживает в городе {args[2]}'
    

def ageinput():
    try:
        age = int(input("Введите возраст человека: "))
        if age < 0:
            print("Возраст не может быть отрицательным числом")
            ageinput()
        elif age > 120:
            print("Столько люди не живут")
        return age

    except ValueError:
        print("Возраст необходимо ввети цифрами")
        ageinput() #да-да, это рекурсия :)


def notnull(value):
    if value == "":
        print("Значение не может быть пустой строкой")
    else:
        return value.capitalize() #первую буквы делаем большой, т.к.  имена собственные должны пистаь с большой
def stopprogramm():
    cancel = input("Повторим? (y/n): ")
    if cancel == "y":
        return False
    elif cancel == "n":
        return True
    else:
        print("Возможные варианты ввода: ""n"" или ""y"".")
        return stopprogramm()


while True:
    name = notnull(input("Введите имя человека: "))
    age = ageinput()
    city = notnull(input("Введите город проживания: "))
    print(fuc(name=f'{name}',age=f'{age}',city=f'{city}')) #именнованные параметры
    print("-" * 50)
    print(fuc2(name,age,city)) #список параметров
    print("-" * 50)
    cancel = stopprogramm()
    if cancel:
        break
