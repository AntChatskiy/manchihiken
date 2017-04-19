"""
Игра в стиле манчкин-квеста с возможностью перемещаться по комнатам 
"""

'''
    Исправил цвета, 0 -- это черный. Нужно использовать 7, белый очеитка экрана работает нормально
    Не хорошо получается что персонаж и монстры одного цвета со стенами. Давай будем красить в другой
    цвет. Тогда про поменяем структуру вывода и не будем объединять в строку массив мира.
    Сначала нужно переписать процедуру draw_world(), чтобы она выводила двумерный массив
    без объединения в строку и отделения каждого элемента ковычками.
    Затем нужно смотреть, если в ячейке не # или " " то пользоваться print_unit() вместо print()
    имеет смысл в положение игрока на карте записывать цифру от 1 до 9, а вместо монстра 10 и более
    функция print_unit() будет проверять значение цисла и если это игрок то выводить его символ и цвет
    свой для каждого игрока.
'''
# TODO  создать функцию print_unit() которая будет менять и выводить символ другого цвета

import ctypes   # библиотека для работы с системной консолью
import os   # библиотека для работы с системными командами
import time     # библиотека для работы с временем
import random  # библиотека для работы со случайностью
# time.sleep(3)  заморозка времени(секунда)


def create_room(world, icon):
    '''
    Переносит персонажа с задержкой в 2 секунды в указанную комнату
    '''
    # массив комнаты
    room = list()

    # создаём комнату
    room.append(['#' for i in range(29)])
    for i in range(12):
        room.append(list())
        room[i + 1].append('#')
        for j in range(27):
            room[i + 1].append(' ')
        room[i + 1].append('#')
    room.append(['#' for i in range(29)])

    #  размещение монстра в комнате

    a = random.randint(1, 12)
    b = random.randint(1, 28)

    if a == 6:
        if b == 13:
            while b == 13:
                b = random.randint(1, 28)

    room[a][b] = '$'

    # дополнительные стены в комнате
    for wall in range(10):
        a = random.randint(1, 12)
        b = random.randint(1, 28)
        if a == 6:
            if b == 13:
                while b == 13:
                    b = random.randint(1, 28)
        room[a][b] = '#'


    while True:

        print('Are u going to travel Y/N? Where?')
        answer = input()
        if answer == 'N':
            break
        place = input()

        title = '         Room '
        if place == 'Room 1':
            world[6][13] = ' '
            world[2][5] = icon
            draw_map(world)
            time.sleep(1)
            world[2][5] = ' '
            room[6][13] = icon
            print(title, '1')
            draw_room(room)

        elif place == 'Room 2':
            world[6][13] = ' '
            world[2][14] = icon
            draw_map(world)
            time.sleep(1)
            world[2][14] = ' '
            room[6][13] = icon
            print(title, '2')
            draw_room(room)

        elif place == 'Room 3':
            world[6][13] = ' '
            world[2][23] = icon
            draw_map(world)
            time.sleep(1)
            world[2][23] = ' '
            room[6][13] = icon
            print(title, '3')
            draw_room(room)

        elif place == 'Room 4':
            world[6][13] = ' '
            world[10][5] = icon
            draw_map(world)
            time.sleep(1)
            world[10][5] = ' '
            room[6][13] = icon
            print(title, '4')
            draw_room(room)

        elif place == 'Room 5':
            world[6][13] = ' '
            world[10][14] = icon
            draw_map(world)
            time.sleep(1)
            world[10][14] = ' '
            room[6][13] = icon
            print(title, '5')
            draw_room(room)

        elif place == 'Room 6':
            world[6][13] = ' '
            world[10][23] = icon
            draw_map(world)
            time.sleep(1)
            world[10][23] = ' '
            room[6][13] = icon
            print(title, '6')
            draw_room(room)

        elif place == 'World':
            room[6][13] = ' '
            draw_room(room)
            time.sleep(1)
            world[6][13] = icon
            draw_map(world)


def draw_room(room):
    '''
     рисует карту комнаты
    '''
    os.system('cls')
    for line in room:
        print(''.join(line))


def draw_world(world):
    '''
    рисует карту мира
    '''
    for line in world:
        print(''.join(line))


def create_world():
    '''
    чтения игрового мира из файла
    '''
    # мапа
    wrd = list()
    file = open('map(1).txt', 'r')

    for line in range(14):
        wrd.append(list(file.readline().rstrip()))
    file.close()

    return wrd


def create_player():
    '''
    Создает персонажа с параметрами имени, пола, расы, уровня, иконы и силы
    '''
    name = input('Enter name: ')
    sex = input('Enter gender (F/M): ')
    hero = {'name': name, 'sex': sex, 'race': 'human', 'lvl': 1,
            'icon': '&', "arm": 1}
    return hero


def show_hero_stat(player):
    '''
    Возвращает инфу персонажа
    '''

    ctypes.windll.Kernel32.GetStdHandle.restype = ctypes.c_ulong
    h = ctypes.windll.Kernel32.GetStdHandle(ctypes.c_ulong(0xfffffff5))

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 4)
    print('name:', end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 7)
    print(player['name'], end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 6)
    print('sex:', end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 7)
    print(player['sex'], end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 14)
    print('race:', end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 7)
    print(player['race'], end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 3)
    print('lvl:', end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 7)
    print(player['lvl'], end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 1)
    print('arm:', end=' ', flush=True)

    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, 7)
    print(player['arm'])
# TODO удалить выполненые TODO!!!!!!!
# TODO Сделать красивое чтение из файла без магии

# Это будет основное тело программы, пока оставь так и назвение файла не меняй, а то работать не будет
# под этим условием организуй основной цикл игры
if __name__ == "__main__":

    player = create_player()
    world = create_world()
    # задание положения персонажа
    world[6][13] = player['icon']
    show_hero_stat(player)


    # карта
    draw_world(world)

    # куда ты идешь
    create_room(world, player['icon'])

    print('U are on the point')




