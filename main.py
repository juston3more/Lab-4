a = []
size = float(3*3) 
start_points = 10 
items = {
'r': [3, 25],
'p': [2, 15],
'a': [2, 15],
'm': [2, 20],
'i': [1, 5],
'k': [1, 15],
'x': [3, 20],
't': [1, 25],
'f': [1, 15],
'd': [1, 10],
's': [2, 20],
'c': [2, 20]
}
for i in items:
    items[i].append(items[i][1]/items[i][0])
items = sorted(items.items(), key=lambda x: x[1][2])
items = items[::-1]
for i in items:
    if (size - float(i[1][0])) >= 0:
        a.append(i[0])
        size = size - float(i[1][0])
        start_points += float(i[1][1])
    else:
        start_points -= float(i[1][1])
print(a)
print('Итоговые очки выживания:', int(start_points))