'''
1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
'''
import random
import fruits

list1 = ["яблоко", "огурец", "груша"]
list2 = ["помидор", "кабачок", "огурец", "маракуя", "огурец", "яблоко"]

'''
Небольшая оптимизация в данной функции: определяем который из списков короче и проходимся по нему, т.о. сокращаем
число проходов.
'''

def do_list(list_first=list1, list_second=list2):
    shortlist = list_first if len(list_first) < len(list_second) else list_second
    longlist = list_first if len(list_first) > len(list_second) else list_second
    totalList = [fruit for fruit in shortlist if fruit in longlist]
    return totalList


def get_fruit_list():
    retlist = []
    for x in range(2):
        first = random.randint(10, len(fruits.all_fruits))
        last = first + len(fruits.all_fruits) - random.randint(1, len(fruits.all_fruits) - 1)
        newlist = fruits.all_fruits[first:last]
        retlist.append(newlist)
        print(f'Список фруктов №{x+1}({len(newlist)} штук)', newlist, sep="\r\n")
    return retlist


def fruitslist(choise):
    if choise == 1:
        tmpres = get_fruit_list()
        res = do_list(tmpres[0], tmpres[1])
        print(f'Совпадений:{len(res)}', res if len(res) > 0 else "Список пуст", sep='\r\n')
    elif choise == 2:
        res = do_list()
        print(f'Совпадений:{len(res)}', res if len(res) > 0 else "Список пуст", sep='\r\n')


if __name__ == "__main__":
    fruitslist(1)
    fruitslist(2)

