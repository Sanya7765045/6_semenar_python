# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

progression = []

# Ввод первого элемента арифметической прогрессии
progression.append(int(input("Введите первый элемент арифметической прогрессии: ")))

# Ввод разности арифметической прогрессии
d = int(input("Введите разность арифметической прогрессии: "))

# Ввод количества членов арифметической прогрессии
n = int(input("Введите количество членов арифметической прогрессии: "))

i = 2

# Заполняем массив арифметической прогрессии
while i <= n:
    # Вычисление n-го члена прогрессии по формуле an = a1 + (n-1) * d
    progression.append(int((i-1) * d + progression[0]))
    i += 1

# Вывод полученной арифметической прогрессии
print(progression)
