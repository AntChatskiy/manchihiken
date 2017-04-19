import ctypes # подключаем библиотеку для работы с системной консолью
ctypes.windll.Kernel32.GetStdHandle.restype = ctypes.c_ulong 
# создаем переменную для обращания к системной консоли
h = ctypes.windll.Kernel32.GetStdHandle(ctypes.c_ulong(0xfffffff5))
for color in range(16):
    # перебераем цифровые обозначения цветов
    # и изменяем значение цвета консоли
    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, color)
    # 
    # хитры способ форматирования вывода, расскажу о не позже
    print ("color {0}".format( color ))