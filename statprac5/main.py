from math import log
from prettytable import PrettyTable
import matplotlib.pyplot as plt

data = [-0.03, 0.73,
        -0.59, -1.59,
        0.38, 1.49,
        0.14, -0.62,
        -1.59, 1.45,
        -0.38, -1.49,
        -0.15, 0.63,
        0.06, -1.59,
        0.61, 0.62,
        -0.05, 1.56]


def get_input_data(data):
    return data


def get_sorted_data(data):
    return sorted(data)


def get_first(data):
    return get_sorted_data(data)[0]


def get_last(data):
    return get_sorted_data(data)[-1]


def razmah(data):
    return round(get_sorted_data(data)[-1] - get_sorted_data(data)[0], 2)


def get_stat_data(data):
    count_set = {}
    for x in get_sorted_data(data):
        if count_set and x == list(count_set.keys())[-1]:
            count_set[x] += 1
        else:
            count_set[x] = 1

    table = PrettyTable()
    table.field_names = ["x(i)", *count_set.keys()]
    table.add_row(["n(i)", *count_set.values()])
    return table


def get_average(data):
    return sum(data) / len(data)


def get_dispersion(data):
    disp = 0
    for x in data:
        disp += pow(x - get_average(data), 2)
    return disp


def get_SKO(data):
    return pow(get_dispersion(data), 0.5)


def draw_func(data):
    count_set = {}
    for x in get_sorted_data(data):
        if count_set and x == list(count_set.keys())[-1]:
            count_set[x] += 1
        else:
            count_set[x] = 1

    plt.subplot(5, 1, 1)
    plt.title("График эмпирической функции распределения")
    n = len(count_set)
    keys = list(count_set.keys())
    y = 0
    print(f'\t\t/ {round(y, 2)}, при x <= {keys[0]}')
    for i in range(n - 1):
        y += count_set[keys[i]] / n if i < n else 0
        left = "F*(x) = " if i == n / 2 else "\t\t"
        print(f'{left}| {round(y, 2)}, при {keys[i]} < x <= {keys[i + 1]}')
        plt.plot([keys[i], keys[i + 1]], [y, y], c = 'black')
    print(f'\t\t\\ {round(y, 2)}, при {keys[-1]} < x')


def get_intervals(data):
    count_set = {}
    for x in get_sorted_data(data):
        if count_set and x == list(count_set.keys())[-1]:
            count_set[x] += 1
        else:
            count_set[x] = 1
    n = len(count_set)
    keys = list(count_set.keys())
    h = round((get_sorted_data(data)[-1] - get_sorted_data(data)[0]) / (1 + round(log(n, 2))), 2)

    curr_x = round(get_sorted_data(data)[0] - h / 2, 2)
    next_x = round(curr_x + h, 2)
    group = {curr_x: 0}
    for x in get_sorted_data(data):
        if x < next_x:
            group[curr_x] += 1 / n
        else:
            group[next_x] = 1 / n
            curr_x = next_x
            next_x = round(next_x + h, 2)
    table = PrettyTable()
    table.field_names = (f'[{round(x, 2)}; {round(x + h, 2)})' for x in group.keys())
    table.add_row(list(round(x, 2) for x in group.values()))
    return table


def get_poligon(data):
    count_set = {}
    for x in get_sorted_data(data):
        if count_set and x == list(count_set.keys())[-1]:
            count_set[x] += 1
        else:
            count_set[x] = 1
    n = len(count_set)
    keys = list(count_set.keys())
    h = round((get_sorted_data(data)[-1] - get_sorted_data(data)[0]) / (1 + round(log(n, 2))), 2)

    curr_x = round(get_sorted_data(data)[0] - h / 2, 2)
    next_x = round(curr_x + h, 2)
    group = {curr_x: 0}

    for x in get_sorted_data(data):
        if x < next_x:
            group[curr_x] += 1 / n
        else:
            group[next_x] = 1 / n
            curr_x = next_x
            next_x = round(next_x + h, 2)
    plt.subplot(5, 1, 3)
    plt.title("Полигон частот")
    plt.plot(list(group.keys()), list(group.values()), c = 'black')


def get_gist(data):
    count_set = {}
    for x in get_sorted_data(data):
        if count_set and x == list(count_set.keys())[-1]:
            count_set[x] += 1
        else:
            count_set[x] = 1
    n = len(count_set)
    keys = list(count_set.keys())
    h = round((get_sorted_data(data)[-1] - get_sorted_data(data)[0]) / (1 + round(log(n, 2))), 2)

    curr_x = round(get_sorted_data(data)[0] - h / 2, 2)
    next_x = round(curr_x + h, 2)
    group = {curr_x: 0}

    for x in get_sorted_data(data):
        if x < next_x:
            group[curr_x] += 1 / n
        else:
            group[next_x] = 1 / n
            curr_x = next_x
            next_x = round(next_x + h, 2)

    plt.subplot(5, 1, 5)
    plt.title("Гистограмма частот")
    plt.bar(list(map(lambda x: x + h / 2, group.keys())), list(group.values()), width = h)
    xticks = list(group.keys()) + [round(list(group.keys())[-1] + h, 2)]
    plt.xticks(xticks, xticks)


def main():
    print("Исходный ряд:")
    print(get_input_data(data))

    print("Вариационный ряд:")
    print(get_sorted_data(data))

    print("Первая порядковая статистика:")
    print(get_first(data))

    print("Последняя порядковая статистика:")
    print(get_last(data))

    print("Размах:")
    print(razmah(data))

    print("Статистический ряд:")
    print(get_stat_data(data))

    print("Выборочное среднее:")
    print(get_average(data))

    print("Дисперсия:")
    print(get_dispersion(data))

    print("СКО:")
    print(get_SKO(data))

    print("Эмпирическая функция:")
    draw_func(data)

    print("Интервальное статистическое распределение:")
    print(get_intervals(data))

    get_poligon(data)

    get_gist(data)

    plt.show()


if __name__ == '__main__':
    main()
