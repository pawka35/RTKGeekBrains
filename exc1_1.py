'''
Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
'''

try:
    userInput = int(input("Введите число: "))
except ValueError:
    print("Вы ввели не число. Попробуйте еще раз")

print("Результат {0}+{1}={2}".format(userInput, 2, userInput+2))
