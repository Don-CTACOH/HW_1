# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     if type(lines) != int or lines <= 0:
#         print("Введите корректное число строк!")
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.read().splitlines()
#         for el in range(len(text) - lines, len(text)):
#             print(text[el])


# lines = int(input("Ведите количество строк: ", ))
# read_last(lines, 'HW_8/article.txt')


# 2. Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def longest_worlds(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        words = (" ".join(text)).split()
        count_dict = {}
        for el in words:
            count_dict[el] = len(el)

        inv_count_dict = {}
        for k, v in count_dict.items():
            inv_count_dict[v] = inv_count_dict.get(v, []) + [k]

        count_max = 0
        for k in inv_count_dict.keys():
            if k > count_max:
                count_max = k
        print(inv_count_dict[count_max])

longest_worlds('HW_8/article.txt')