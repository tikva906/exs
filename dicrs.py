user = {"name": "Niok3",
        "age": 39,
        "cars": ["BMW", "Audi"]}

print(user.keys())
for k in user.keys():
        if k == "cars":
                for car in user[k]:
                        print(car)
        else:
                print(user[k])


print(user.values())
for v in user.values():
        print(v)

for k,v in user.items():
        if k == "cars":
                for car in v:
                        print(car)
        else:
                print(v)