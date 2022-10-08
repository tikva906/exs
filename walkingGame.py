import os

from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Player:
    def __init__(self, name):
        self.Name = name
        self.x = 0
        self.y = 0
        self.score = 0

    def Up(self):
        self.x += 1

    def Down(self):
        self.x -= 1

    def Left(self):
       self.y -= 1

    def Right(self):
        self.y += 1

# Сколько врагов спавнить
mobSettings = {1: {'количество': (20,50), 'уровень': (1,20)},
               2: {'количество': (10,30), 'уровень': (8,60)},
               3: {'количество': (5,10), 'уровень': (10,100)}}
# Размеры карт
mapSettings = {1: 10, 2: 7, 3: 5}

# Сколько спавнится яблок
appleSettings = {1: (2,5), 2: (1,3), 3: (1,2)}

# текущий уровень
level = 3


map = []

for i in range(mapSettings[level]):
    map.append([])
    for j in range(mapSettings[level]):
        map[i].append('.')

def GenerateEliment(element):
    if element == '@':
        a = appleSettings[level][0]
        b = appleSettings[level][1]
    else:
        a = mobSettings[level]['количество'][0]
        b = mobSettings[level]['количество'][1]
    for i in range(randint(a, b)):
        x = randint(0, len(map) - 1)
        y = randint(0, len(map) - 1)
        if map[x][y] == '.':
            if element == '@':
                map[x][y] = element
            elif element == 'mob':
                map[x][y] = randint(mobSettings[level]['уровень'][0],mobSettings[level]['уровень'][1])
def ShowMap():
    for el in map[::-1]:
        for e in el:
            print(e, end="\t")
        print()

def ShowPoint(x,y):
    map[x][y] = 'x'

def ClearPoint(x,y):
    map[x][y] = '.'

pleer = Player('tikovka906')
ShowPoint(pleer.x, pleer.y)
GenerateEliment('@')
GenerateEliment('mob')
ShowMap()
while True:
    print(f'Ваш счет: {pleer.score}')
    go = input(">> ")
    ClearPoint(pleer.x, pleer.y)
    if go == "w":
        pleer.Up()
    elif go == 's':
        pleer.Down()
    elif go == 'a':
        pleer.Left()
    elif go == 'd':
        pleer.Right()
    if map[pleer.x][pleer.y] == '@':
        pleer.score += 1
        GenerateEliment('@')
    elif map[pleer.x][pleer.y] != '.':
        if map[pleer.x][pleer.y] >= pleer.score:
            break
        else:
            pleer.score += map[pleer.x][pleer.y]
    ShowPoint(pleer.x, pleer.y)
    cls()
    ShowMap()

print(f'ВЫ ПРОИГРАЛИ!\nВаш счет: {pleer.score}')