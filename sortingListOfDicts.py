players = [{"name": "Nik83", "lvl": 19},
    {"name": "Fol83", "lvl": 5},
    {"name": "Dm3455", "lvl": 1},
    {"name": "Ololo", "lvl": 17}]

for i in range(0,len(players)):
    min = players[i]    ["lvl"]
    now = min
    k = i
    for j in range(i + 1,len(players)):
        now = players[j]["lvl"]
        if now < min:
            min = now
            k = j
    tmp = players[i]
    players[i] = players[k]
    players[k] = tmp

for p in players:
    print(p)`