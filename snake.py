# Класс Snake
# def init: параметр Name
#         параметр по умолчанию: self.BodyCoords = [(1,1),(1,2),(1,3)]

# def Up(), def Down(), def Left(), def Right()
import os
from random import randint

class Snake:
    def __init__(self,name):
        self.Name = name
        self.score = 0
        # Набоор координат туловища змейки - список кортежей, кортеж - пара координат (x,y)
        self.BodyCoords = [(1,1),(1,2),(1,3)]


    def EatApple(self, x, y):
        self.BodyCoords.append((x,y))
        self.score += 1

    def Right(self):
        # Убираем координаты кончика хвоста
        del self.BodyCoords[0]
        # Создаем новый набор координат (куда пошла змейка)
        # змейка идет вправо => от головы X меняется на +1, а Y остается такой же
        x = self.BodyCoords[-1][0]+1
        y = self.BodyCoords[-1][1]
        # Добавляем новую позицию головы змейки в BodyCoords
        self.BodyCoords.append((x,y))

    def Left(self):
        del self.BodyCoords[0]
        x = self.BodyCoords[-1][0]-1
        y = self.BodyCoords[-1][1]
        self.BodyCoords.append((x,y))

    def Up(self):
        del self.BodyCoords[0]
        x = self.BodyCoords[-1][0]
        y = self.BodyCoords[-1][1]+1
        self.BodyCoords.append((x,y))

    def Down(self):
        del self.BodyCoords[0]
        x = self.BodyCoords[-1][0]
        y = self.BodyCoords[-1][1]-1
        self.BodyCoords.append((x,y))



def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def GenerateMap(n):
    map = []
    for i in range(n):
        map.append([])
        for j in range(n):
            map[i].append(' ')
    return map

def SetBorders(map):
    for i in range(0,len(map)):
        map[0][i] = '#'
        map[-1][i] = '#'
    for i in range(1,len(map) -1):
        map[i][0] = '#'
        map[i][-1]= '#'

def ShowMap(map):
    for el in map[::-1]:
        for e in el:
            print(e, end=" ")
        print()

def GenerateApple(map):
    count = randint(1, 2)
    spawned = False
    for i in range(0, count):
        x = randint(1, len(map) - 2)
        y = randint(1, len(map) - 2)
        if map[x][y] != 'x' and map[x][y] != "%":
            map[x][y] = '@'
            spawned = True
    if spawned == False:
        GenerateApple(map)

def FillEmpties(map):
    for i in range(1,len(map) -1):
        for j in range(1, len(map) - 1):
            if map[i][j] == " " and (map[i+1][j] == "%" or map[i+1][j] == "#") and (map[i][j -1] == "%" or map[i][j-1] == "#") and (map[i][j +1] == "%" or map[i ][j+1] == "#") and (map[i - 1][j] == "%" or map[i - 1][j] == "#"):
                map[i][j] = '%'

def GenerateBarrier(map):
    count = ((len(map) - 2)**2)//4
    for i in range(0, count):
        x = randint(1, len(map) - 2)
        y = randint(1, len(map) - 2)
        if map[x][y] != 'x' and map[x][y] != '@':
            map[x][y] = '%'

def SetSnake(snake,map):
    # Проходим все координаты змейки, и в таких же координатах карты устанавливаем X
    for coords in snake.BodyCoords:
        # X на карте - это У у змейкиw
        # Y на карте - это X у змейки
        map[coords[1]][coords[0]] = 'x'

def ClearOldCoords(oldCoords):
    map[oldCoords[1]][oldCoords[0]] = ' '

# Функция CheckWin(snake, map)
# если размер бадикорс == (размеру карты - 1 )**2
#      то return True
# иначе возвращаешь False

def CheckWin(snake, map):
    if len(snake.BodyCoords) == (len(map) - 2)**2:
        return True
    else:
        return False

def CheckWin2(map):
    # пройти циклами for карту, и если наталкиваешься на элемент ' ', то вовзраешь true
    for sublist in map:
        for l in sublist:
            if l == ' ':
                return False
    return True

if __name__ == "__main__":
    win = False
    snake = Snake("Змейка")
    map = GenerateMap(20)
    SetBorders(map)
    SetSnake(snake,map)
    GenerateApple(map)
    GenerateBarrier(map)
    FillEmpties(map)
    ShowMap(map)

    while True:
        cmd = input(">> ")
        ClearOldCoords(snake.BodyCoords[0])
        if cmd == "w":
            snake.Up()
        elif cmd == 's':
            snake.Down()
        elif cmd == 'a':
            snake.Left()
        elif cmd == 'd':
            snake.Right()
        cls()

        a = 1

        if map[snake.BodyCoords[-1][1]][snake.BodyCoords[-1][0]] == '@':
            snake.EatApple(snake.BodyCoords[-1][0],snake.BodyCoords[-1][1])
            GenerateApple(map)
            a = 2

        if map[snake.BodyCoords[-1][1]][snake.BodyCoords[-1][0]] == '#' or map[snake.BodyCoords[-1][1]][snake.BodyCoords[-1][0]] == "%":
            break

        if snake.BodyCoords[-1] in snake.BodyCoords[0:len(snake.BodyCoords)-a]:
            cord = 0
            for i in range(len(snake.BodyCoords)):
                if snake.BodyCoords[-1] == snake.BodyCoords[i]:
                    cord = i
                    break
            bkcopi = snake.BodyCoords[0:cord]

            snake.BodyCoords = snake.BodyCoords[cord:len(snake.BodyCoords)]

            for xy in bkcopi:
                map[xy[1]][xy[0]] = " "


        SetSnake(snake, map)
        ShowMap(map)
        print(f"Счет: {snake.score}")

        win = CheckWin2(map)

        if win == True:
            break

    # ДЗ:a
    # Подумать о том, как сделать условие выигрыша
    # Что такое заполнить все клетки?

    if win == True:
        print('Вы победили')
    else:
        print('Вы пороиграли')

    print(f"Счет: {snake.score}")

