import random

from snake import GenerateMap, GenerateBarrier, SetBorders, ShowMap


'''map = [['#', '#', '#', '#', '#', '#', '#'],
       ['#', ' ', ' ', ' ', ' ', ' ', '#'],
       ['#', ' ', ' ', '%', ' ', ' ', '#'],
       ['#', ' ', '%', ' ', '%', ' ', '#'],
       ['#', ' ', ' ', '%', ' ', '%', '#'],
       ['#', ' ', ' ', ' ', '%', ' ', '#'],
       ['#', '#', '#', '#', '#', '#', '#']]'''


def FillEmpties(map):
    empties = 0
    for i in range(1,len(map) -1):
        for j in range(1, len(map) - 1):
            if map[i][j] == " " and (map[i+1][j] == "%" or map[i+1][j] == "#") and (map[i][j -1] == "%" or map[i][j-1] == "#") and (map[i][j +1] == "%" or map[i ][j+1] == "#") and (map[i - 1][j] == "%" or map[i - 1][j] == "#"):
                map[i][j] = '%'
                empties += 1
    return empties

def CheckEmpties(map):
    badCount = 0
    for i in range(1,len(map) -1):
        for j in range(1, len(map) - 1):
            if map[i][j] == " " and (map[i+1][j] == "%" or map[i+1][j] == "#") and (map[i][j -1] == "%" or map[i][j-1] == "#") and (map[i][j +1] == "%" or map[i ][j+1] == "#") and (map[i - 1][j] == "%" or map[i - 1][j] == "#"):
                badCount += 1
    return badCount


count = 1
mistakes = False
while (count <= 500):
    n = random.randint(10, 40)
    map = GenerateMap(n)
    SetBorders(map)
    GenerateBarrier(map)
    empties = FillEmpties(map)
    bad = CheckEmpties(map)
    if empties > 0:
        print(f"Тест {count}: {empties}")
    if (bad > 0):
        print(f"Тест {count}: {bad}")
        ShowMap(map)
        mistakes = True
    count += 1

if mistakes == False:
    print("Ошибок нет.")