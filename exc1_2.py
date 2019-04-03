'''
Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
'''

condition = True

while condition:
    try:
        userInput = int(input("Введите число от 0 до 10: "))
    except ValueError:
        print("Вы ввели не число, давайте попробуем еще раз.")
        continue
    if userInput > 10 or userInput < 0:
        print("Необходимо ввести число от 0 до 10")
        print("Введеное число {0} не входит в данный диапазон.".format(userInput))
        print("Попробуйте еще раз.")
    else:
        print("Результат:{0} в степени 2={1}".format(userInput, userInput ** 2))
        print("Закончили упражнение")
        condition = False

