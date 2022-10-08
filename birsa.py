currency1 = {"name": "доллар",
             "values": [30, 45, 70, 90, 70]}

currency2 = {'name': 'юань',
             'values': [11, 8, 3, 6, 9, 10, 11, 2, 3, 4, 5]}

currencies = []

currencies.append(currency1)
currencies.append(currency2)


while True:
    command = input('>> ')
    if command == "/currencies":
        print("СПИСОК ВАЛЮТ: ")
        number = 1
        for currency in currencies:
            print(f'\t{number}. {currency["name"]}')
            number += 1
    elif command == "/stats":
        currencyInput = input('Введите валюту для просмотра статистики: ')
        avverage = 0
        for currency in currencies:
            if currency['name'] == currencyInput:
                sum = 0
                count = len(currency['values'])
                for value in currency['values']:
                    sum += value
                avverage = sum/count
                print(f"\tСредний курс {currency['name']}: {avverage} рублей")
    elif command == "/addvalue":
        currencyInput = input("Ввведите валюту: ")
        for currency in currencies:
            if currency["name"] == currencyInput:
                value = int(input("\tВведите курс на текущий момент: "))
                currency["values"].append(value)
                print("\t\tУспешное обновление!")
    elif command == "/course":
        currencyInput = input("Введите валюту: ")
        for currency in currencies:
            if currency["name"]== currencyInput:
                print(f"\tТекущий курс: {currency['values'][-1]} рублей")

    elif command == "/exit":
        break
    else:
        print("Такой команды не существует!")