import random

# массив комнаты
room = list()
# создаём комнату
room.append(['#' for i in range(29)])
for i in range(12):
    room.append(list())
    room[i + 1].append('#')
    for j in range(27):
        room[i+1].append(' ')
    room[i + 1].append('#')
room.append(['#' for i in range(29)])

# монстр в комнате
for monster in range(2):
    a = random.randint(1, 12)
    b = random.randint(1, 28)
    if a == 6:
        if b == 13:
            while b == 13:
                b = random.randint(1, 28)
    room[a][b] = '$'
# стены в комнате
for wall in range(10):
    a = random.randint(1, 12)
    b = random.randint(1, 28)
    if a == 6:
        if b == 13:
            while b == 13:
                b = random.randint(1, 28)
    room[a][b] = '#'
