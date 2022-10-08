# Item - name, count, maxCount
class Item:
    def __init__(self,name,count,maxCount):
        self.Name = name
        self.Count = count
        self.MaxCount = maxCount


inv = [None, Item('алмаз', 27, 64), None, Item('око края',16,64),Item('уголь',56,64),Item('уголь',34,64),Item('нежок',13,16),None,None]

print('До распределения: ')
for item in inv:
    if item != None:
        print(f"{item.Name}: {item.Count}/{item.MaxCount}")
    else:
        print("Пусто")

name = input('Название предмета для распредления: ')
count = int(input('Введите количество придметов: '))
maxCount = int(input('Введите максимальное число: '))

toAdd = Item(name, count, maxCount)

for i in range(0, len(inv)):
    if inv[i] != None:
        if inv[i].Name == toAdd.Name:
            max_add = inv[i].MaxCount - inv[i].Count

            if max_add >= toAdd.Count:
                inv[i].Count += toAdd.Count
                toAdd.Count = 0
            else:
                inv[i].Count += max_add
                toAdd.Count -= max_add

for i in range(0,len(inv)):
    if inv[i] == None:
        if toAdd.Count >= toAdd.MaxCount:
            inv[i] = Item(toAdd.Name, toAdd.MaxCount, toAdd.MaxCount)
            toAdd.Count -= toAdd.MaxCount
        else:
            if toAdd.Count != 0:
                inv[i] = Item(toAdd.Name, toAdd.Count, toAdd.MaxCount)
                toAdd.Count = 0

print('после распредиления: ')
for item in inv:
    if item != None:
        print(f"{item.Name}: {item.Count}/{item.MaxCount}")
    else:
        print("Пусто")