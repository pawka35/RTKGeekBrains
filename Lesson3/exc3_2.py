'''
Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

От себя:
- проверка корректности ввода
- первый сопособ - в функцию передается список чисел
- второй способ - чтобы дословно выполнить задание - в функцию передаются 3 отдельных числа
'''

list = []
count_pop = 0

def getvalue():
    try: 
        value = int(input(f'Введите число: '))
    except ValueError:
        print("Введено не число. Попробуйте еще раз")
        value =  getvalue()
    return value

def maximum(list): 
    return max(list)

def maximum_second_ed(a,b,c):
    return max(a,b,c)

    
for x in range(3):
    list.append(getvalue())


print(f'Наибольшим из набора чисел: {list}, является число: {maximum(list)}')

print("="*50)
print("Второй способ") #если дословно следовать условию задачи, то мы должны в функцию передать не список, а именно 3 числа

a = getvalue()
b = getvalue()
c = getvalue()
print(f'Наибольшим из набора чисел: {list}, является число: {maximum_second_ed(a,b,c)}')
