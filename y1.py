import sys
# Класс DesktopApp
#       init: name
#             Параметры по умолчанию: width, height (ширина, высота)
# Методы:
#       def close: закрыть приложение (организовать с помощью print())
#       def collapse: свернуть приложение
#       def stretch_width: шиирина увеличивается на 1
#       def stretch_height: высота увеличивается на 1
class DesktopApp:
    def __init__(self,name):
        self.Name = name
        self.width = 300
        self.height = 400
    def close(self):
        print('завершение работ')
        sys.exit()


    def collapse(self):
        print('приложение свернулось')

    def stretch_width(self):
        self.width += 1

    def stretch_height(self):
        self.height += 1


# Создать объект DesktopApp
app = DesktopApp('free fire')
while True:
    command = input('>> ')
    if command == '/info':
        print(f'Название: {app.Name} ширина {app.height} , {app.width}')

    elif command == '/stratchWidth':
        app.stretch_width()

    elif command == '/stratchHeight':
        app.stretch_height()

    elif command == '/close':
        app.close()
    elif command == '/collapse':
        app.collapse()

# Цикл while True, который ожидает ввода команд
# Перечень команд: /info - вывести информацию о приложении, его ширине, высоте и названии
#                   /stratchWitdh - растянуть влево
#                   /stratchHeight - вправо
#                   /close - вызов метода close
#                   /collapse - свертывание