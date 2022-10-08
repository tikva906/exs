lesson1 = {"name": "математека",
             "estimates": [5,2,5,5]}

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

while True:
    command = input('>> ')
    if command == "/addvalue":
        lessonInput = input("Введите урок: ")
        for lesson in lessons:
            if lesson["name"] == lessonInput:
                estimat = int(input("\tВведите оттенку которую хотите добавить: "))
                lesson["estimates"].append(estimat)
                print("\t\tУспешное обновление!")
    elif command == "/shades":
        lessonInput = input("Введите урок: ")
        for lesson in lessons:
            if lesson["name"] == lessonInput:
                print(f"\tТекущяя оттенка: {lesson['estimates'][-1]} оттенок")