class Cat:
    def __init__(self, name, color):
        self.Name = name
        self.Color = color


def Ser(cat):
    return Cat(cat['Name'], cat['Color'])

def Deser(cat):
    return {'Name': cat.Name, 'Color': cat.Color}

cat = Cat('Мурзик', 'оранжевый')

carDeser = Deser(cat)
print(carDeser)

print(Ser(carDeser))
