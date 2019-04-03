'''
Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.
'''

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]


for x in my_list_2:
    while True:
        result = x in my_list_1
        if not result:
            break
        my_list_1.remove(x)

print(my_list_1)
