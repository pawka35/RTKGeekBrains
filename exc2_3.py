'''
Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
'''

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

res_list = []
for x in my_list_1:
    if my_list_1.count(x) == 1:
        res_list.append(x)

print(res_list)
