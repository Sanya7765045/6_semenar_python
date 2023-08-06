import random

def createRandomList(number_of_list):
    """
    Функция создает список с заданным количеством элементов.

    Аргументы:
    number_of_list -- количество элементов в списке

    Возвращает:
    Список, заполненный рандомными элементами.
    """
    my_list = []
    for i in range(number_of_list):
        my_list.append(random.randint(0, 10))
    print(*my_list)
    return my_list

number_of_list = int(input("Введите количество элементов массива: "))
i = int(input("Введите начало диапазона: "))
j = int(input("Введите конец диапазона: "))
my_list = createRandomList(number_of_list)
index_list = []

print(my_list)

for index, k in enumerate(my_list):  # Используем enumerate() для получения индексов и элементов
    if k >= i and k <= j:
        index_list.append(index)

print("Индексы элементов, значения которых принадлежат заданному диапазону:")
print(*index_list)
