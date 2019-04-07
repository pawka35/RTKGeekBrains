'''
Давайте усложним предыдущее задание.  Измените сущности, добавив новый
параметр — armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать
полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
1.  Наносит урон.  Это улучшенная версия функции из задачи 3.
2.  Вычисляет урон по отношению к броне.
Примечание.  Функция номер 2 используется внутри функции номер 1 для
вычисления урона и вычитания его из здоровья персонажа.

добавлено от себя:
 - случайная генерация значений урона и брони для каждого игрока
 - ведущий определяет, какой из игроков сделает ход первым
 - урон наносимый игроком корректируется(уменьшается, либо увеличивается) на некую случайную величину каждый ход
 - игроки обмениваются ударами по очереди, пока у одного из них значение здоровья не станет отрицательной величиной
 - в конце игры выводится кто победил и за сколько ходов
 - словарик для удобного вывода показаталей игроков
'''

import random

player = {"name":"", "health": 100, "damage":None, "armor": None}
translator = {"name":"Имя", "health": "Здоровье", "damage":"Урон", "armor": "Броня"}
players = []


def initialisation(player): # генерируем показатели бойца
    player["damage"] = random.randint(10,100)
    player["armor"] = random.randint(100,200) / 100

def tryluck(player): #увеличиваем, либо уменьшаем урон случайным образом
    coef = (random.randint(1,200)) / 100
    dam = player["damage"]
    if(coef > 1):
        print(f"Везет сильнейшим! Урон будет увеличен на  {(coef*100)-100}% от базового ({dam}) и составит {round(dam*coef,2)}")
    else:
        print(f'Небеса сегодня благосклонны к жертве. Урон будет уменьшен на {coef*100}% от базового  ({dam}) и составит {round(dam - dam*coef,2)}')
    return coef

def arrmor_defence(player,damage):
    damage1 = round(damage/player["armor"],2)
    print(f'Броня бойца погасила удар на {round(damage-damage1,2)}')
    return damage1
    

def atack(victim, hunter):
    print(f'Боец {hunter["name"]} атакует бойца {victim["name"]}')
    damage = round(hunter["damage"] * tryluck(hunter),2)
    damage = arrmor_defence(victim, damage)
    print(f'У бойца {victim["name"]} было {round(victim["health"],2)} единиц здоровья')
    victim["health"] -= damage
    print(f"Урон составил: {damage}")
    print(f'У бойца {victim["name"]} стало {round(victim["health"],2)} единиц здоровья')



def player_stats(player):
    for k,v in player.items():
      print(f'{translator[k]}: {v}')


def select_first():
    value = input("Введите номер бойца, который начинает схватку: ")
    try:
        first = int(value)
        if first > len(players):
            print(f"У нас всего {len(players)} бойцов")
            select_first()
    except ValueError:
        print("Необходимо ввести номер бойца:")
        return select_first()
    return first

     
players.append(player)
players.append(player.copy())

pcount = 1

for x in players:
    x["name"] = input(f"Задайте имя игрока {pcount}: ").capitalize()
    initialisation(x)
    print("Бойцу были сгенерированы следующие характеристики: ")
    player_stats(x)
    pcount+=1

first = select_first()

counter = 0
winner, luser = None, None
while True:
    counter+=1
    print("="*50)
    print(f'Ход номер {counter}')
    print("="*50)
    if first == 2:
        if players[1]["health"] > 0:
            atack(players[0],players[1])
        if players[0]["health"] > 0:
            atack(players[1],players[0])
        else: 
            winner = players[1]
            loser = players[0]
            break
    else:
        if players[0]["health"] > 0:
            atack(players[1],players[0])
        if players[1]["health"] > 0:
            atack(players[0],players[1])
        else:
            winner = players[0]
            loser = players[1]
            break

print("=|"*30)
print(f'Победил боец {winner["name"]} за {counter} ходов')


