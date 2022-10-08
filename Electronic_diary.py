lesson1 = {"name": "математека",
             "estimates": []}

lesson2 = {'name': 'русский',
             'estimates': [4,3,3,3,4,4,4,5,]}


lesson3 = {'name': 'китайский',
             'estimates': [4,4,4,4,4,4,4,5]}


lesson4 = {'name': 'литература',
             'estimates': [4,5,5,4,4]}


lesson5 = {'name': 'физкультура',
             'estimates': [5,5,5,5,5,5,5,5,5,5]}
lessons = []
lessons.append(lesson1)
lessons.append(lesson2)
lessons.append(lesson3)
lessons.append(lesson4)
lessons.append(lesson5)

def ShowLessons():
    for Leson in lessons:
        for k,v in Leson.items():
            if k == 'name':
                print(f'\t-{v}')

def reselt(lessonName):
    for lesson in lessons:
        if lesson['name'] == lessonName:
            estimates = lesson['estimates']
            sum = 0
            for estimate in estimates:
                sum += estimate
            count = len(estimates)
            return sum/count
    return None



print("Основные команды - /?")
while True:
    command = input('>> ')
    if command == "/addvalue":
        lessonInput = input("Введите урок: ")
        for lesson in lessons:
            if lesson["name"] == lessonInput:
                try:
                    estimat = int(input("\tВведите оценку которую хотите добавить: "))
                    if estimat <6 and estimat >1:
                        lesson["estimates"].append(estimat)
                        print("\t\tУспешное обновление!")
                    else:
                        print('Вы можете вводить оценки от 2 до 5')
                except:
                    print('Некорректные данные.')
    elif command == "/shades":
        lessonInput = input("Введите урок: ")
        try:
            res = reselt(lessonInput)
            if res != None:
                print(f"\tТекущая оценка: {round(res)}")

            else:
                print("Такого урока нет.")
        except ZeroDivisionError:
            print("Невозможно вычислить оценку.")

    elif command == "/q":
        break
    elif command == '/lessons':
        ShowLessons()
    elif command == "/?":
        print("\t - /lessons - просмотр уроков")
        print("\t - /q - выход")
    else:
        print("Команды не существует!")