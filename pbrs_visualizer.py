import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def prbs_17(sequence_length=131088):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b1000_0000_0000_0000_0  # Пример начального состояния (может быть любым, кроме 0)
    register = 0b0000_0000_0000_0000_1  # Пример начального состояния (может быть любым, кроме 0)
    register = 0b1110_0000_0000_0000_0  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 17, 3)
        new_bit = ((register >> 16) ^ (register >> 2)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b1111_1111_1111_1111_1  # Обрезка до 17 бит
        prbs.append(new_bit)
    print(len(prbs))
    return prbs

def test():
    prbs = prbs_17()
    part = prbs[4:21]
    v = 0
    for i, p in enumerate(part):
        v += (p << (16 - i))  
    print(part, v)

def convert_to_int(value: list):
    l = len(value)
    result = 0
    for i, v in enumerate(value):
        result += (v << (l - 1 - i))
    return result

def test_prbs():
    prbs = prbs_17()
    i = 0
    x = []
    y = []
    while i < (len(prbs) - 16):
        part = prbs[i:i+17]
        i += 1
        x.append(i)
        y.append(convert_to_int(part))

    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.scatter(x, y, s=1)  # Plot some data on the Axes.
    plt.show()

    print(len(part))
if __name__ == '__main__':
    test_prbs()