tisla = [5,3,2,2,8,8,8,5]

# 5
# 2 3 5 2 8 8 8 5

# 3
# 2 2 5 3 8 8 8 5

# 5
# 2 2 3 5 8 8 8 5

# 8
# 2 2 3 5 5 8 8 8


for i in range(0,len(tisla)):
    min = tisla[i]
    now = min
    k = i
    for j in range(i + 1,len(tisla)):
        now = tisla[j]
        if now < min:
            min = now
            k = j
    tmp = tisla[i]
    tisla[i] = tisla[k]
    tisla[k] = tmp

print(tisla)