'''
Создайте программу «Медицинская анкета», где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
Выведите результат согласно которому:
1. Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
2. Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг,
3. Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
'''

def inputcheck(value):
    try:
        int(value)
        return True, int(value)
    except ValueError:
        print("Необходимо ввести число")
        return False,None


def healthconditions(age, weight):
    if 50 < weight or weight < 120:
        if age < 30:
            if weight > 120:
                return "данный  случай не описан в условии, но мне кажется, вы тяжеловаты"
            elif weight < 50:
                return "данный  случай не описан в условии, но мне кажется, надо чуть больше кушать"
        if 30 < age or age < 40:
            return "следует заняться собой"
        if age >= 40:
            return "следует обратиться к врачу"
        if age > 120:
            return "столько не живут. Введите корректный возраст"
    else:
        return "хорошее состояние"


condition = False
fio = input("Введие Ф.И.О пациента: ")

while not condition:
    checked = inputcheck(input("Введите возраст пациента: "))
    age, condition = checked[1], checked[0]
    if age < 0:
         print("Человек не может быть отрицательного возраста. Введите корректный возраст.")
         condition = False
    elif age > 120:
        print("столько не живут. Введите корректный возраст")
        condition = False


condition = False

while not condition:
    checked = inputcheck(input("Введите вес пациента: "))
    weight, condition = checked[1], checked[0]
    if weight < 0:
        print("Человек не может иметь отрицательную массу")
        condition = False


print("{0},{1} год, вес {2} - {3}".format(fio, age, weight, healthconditions(age, weight)))
