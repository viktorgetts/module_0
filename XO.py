import numpy as np


def binary_search(number):  # Создаем функцию бинарного поиска

    bottom_range = 1  # Вводим нижнюю границу диапазона поиска - вначале от 1
    upper_range = 100  # Вводим верхнюю границу диапазона поиска - вначале до 100
    predict = 50  # Допустим, что угадываемое число 50
    count = 1  # Создаем счетчик. С единицы, потому что если число 50, вернется 1 попытка

    while predict != number:  # Пока не угадали число, будет выполняться цикл

        if predict > number:
            upper_range = predict  # Если предполагаемое число больше загаданного, берем диапазон от нижней границы
            # до предполагаемого числа
        elif predict < number:
            bottom_range = predict + 1  # Если меньше - диапазон от предполагаемого числа до верхней границы
        count += 1
        predict = (bottom_range + upper_range) // 2  # Новое предполагаемое число - середина нового диапазона

    return count


def score_game(binary_search):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(binary_search(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(binary_search)
