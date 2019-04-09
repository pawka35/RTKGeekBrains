def check_value(value, number_of_el, operation):

    if (operation == "continue"):
        if value != 'y' and value != 'n':
                print("Возможные варианты ""y"" или ""n"": ")
                return check_value(input(),None,"continue")
        elif value == 'y':
            return True
        elif value == 'n':
            return False

    try:
        value = int(value)
        if  operation == "entervariant" and (value > number_of_el or value <= 0):
            print("Предусмотрено всего 4 варианта выбора: ")
            check_value(input(),4,"entervariant")
    except ValueError:
        if (operation == "enternumbers"):
            return check_value(input(f'Введите элемент №{number_of_el+1}: '),number_of_el,"enternumbers")
        elif (operation == "entercounts"):
            return check_value(input(f' Количество элементов должно быть числом: '),None,"entercounts")
        elif (operation == "entervariant"):
            return check_value(input(f'Вариант должен быть числом: '),4,"entervariant")
       
    return value


