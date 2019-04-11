'''
модуль для добавление информации в файл json
'''

def addtojson():
    example={'name': "", 'tracks': [], 'Albums': [{'name': "", 'year': None}]}

    example['name'] = input('Название группы: ')
    example['tracks'] = input('Название песен (через запятую): ').split(',')

    tmpalb = input('Название альбомов (альбом:год), через запятую').split(',')
    alblist = []
    for x in tmpalb:
        my = {"name": "", "year": ""}
        curalb = x.split(':')
        my['name'] = curalb[0]
        my['year'] = curalb[1]
        alblist.append(my)
    example['Albums'] = alblist
    return example

