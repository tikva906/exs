class Cat:
    def __init__(self, name):
        self.Name = name
        self.Type = "Игривый"

    def Miay(self, count):
        print(f"{self.Name} мяукнул {count} раз.")

cat = Cat("Мурзик")
cat2 = Cat("Кузя")
cat.Miay(10)
cat2.Miay(34)


# Класс Player, в конструктор передаем имя персонажа, по умолчанию x = 0, y = 0
# Методы: Up(), Down(), Left(), Right()

class Player:
    def __init__(self, name):
        self.Name = name
        self.x = 0
        self.y = 0

    def Up(self):
        self.x += 1

    def Down(self):
        self.x -= 1

    def Left(self):
       self.y -= 1

    def Right(self):
        self.y += 1

pleer = Player('tikovka906')

while True:
    go = input(">> ")
    if go == "w":
        pleer.Up()
    elif go == 's':
        pleer.Down()
    elif go == 'a':
        pleer.Left()
    elif go == 'd':
        pleer.Right()
    print(f'{pleer.Name} находится на ({pleer.x},{pleer.y})')