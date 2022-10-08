hleda = [0,1,6,0,43,56,0,64]

toAdd = int(input("Кол-во хлеба для распределения: "))

for i in range(0, len(hleda)):
    if hleda[i] != 0:
        max_add = 64 - hleda[i]

        if max_add >= toAdd:
            hleda[i] += toAdd
            toAdd = 0
        else:
            hleda[i] += max_add
            toAdd -= max_add

for i in range(0,len(hleda)):
    if hleda[i] == 0:
        if toAdd >= 64:
            hleda[i] += 64
            toAdd -= 64
        else:
            hleda[i] += toAdd
            toAdd = 0

print("Ваш инвентарь: ")
print(hleda)
print(f"Кол-во оставшихся в сундуке предметов: {toAdd}")