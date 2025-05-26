def prbs(seed, polynome, length):
    register = seed
    sequence = []
    for _ in range(length):
        feedback = 0
        for i in polynome[1:]:
            feedback ^= (register >> (polynome[0] - i - 1)) & 1
        register = ((register << 1) | feedback) & ((1 << polynome[0]) - 1)
        sequence.append(feedback)
    return sequence

# def get_feedback(register, polynome):
    
#   for i in polynome[:-1]:


def lfsr_Fibonacci(seed, polynome, length):
    register = seed
    sequence = []
    for j, _ in enumerate(range(length)):
        print(j, bin(register))
        sequence.append(register & 1)
        feedback = 0
        for i in polynome[:-1]:
            feedback ^= ((register >> (i - 1)) & 1)
        print(f'{feedback = }')
        print(bin(register >> 1), bin(feedback << (polynome[0] - 1)))
        register = (register >> 1) | (feedback << (polynome[0] - 1))
    return sequence

def lfsr_Fibonacci_2(seed, polynome, length):
    register = seed
    sequence = []
    for j, _ in enumerate(range(length)):
        print(j, bin(register))
        sequence.append(register & 1)
        feedback = 0
        for i in polynome[:-1]:
            feedback ^= ((register >> (i - 1)) & 1)
        # print(f'{feedback = }')
        # print(bin(register >> 1), bin(feedback << (polynome[0] - 1)))
        register = ((register << 1) | feedback) & 0b111
    return sequence

def test_sequence(sequence, window):
    table = {}
    for i in range(len(sequence) - window):
        key = tuple(sequence[i:i+window])
        # print(key)
        if key in table:
            table[key].append(i)
        else:
            table[key] = [i]
        for key, value in table.items():
            if len(value) > 1:
                print(f'{key} appears {len(value)} times.')
    sorted_values = sorted([el[0] for el in table.values()])
    zeros = [i - el for i, el in  enumerate(sorted_values)]
    # print(len(sorted_values))
    # print(zeros)
    # print(*, sep='\n')
    return table

def prbs12(sequence_length=4095):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b110101010101  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 12, 6, 4, 1)
        new_bit = ((register >> 11) ^ (register >> 5) ^ (register >> 3) ^ register) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0xFFF  # Обрезка до 12 бит
        prbs.append(new_bit)
    
    return prbs

def prbs_12(sequence_length=4107):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b100000000000  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 12, 7, 4, 3)
        new_bit = ((register >> 11) ^ (register >> 6) ^ (register >> 3) ^ (register >> 2)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0xFFF  # Обрезка до 12 бит
        prbs.append(new_bit)
    
    return prbs

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

def find_seed_17(subsequence='1'*17):
    sequence_length = len(subsequence)
    for i in range(1, 2**17-1):
        register = i  # Пример начального состояния (может быть любым, кроме 0)
        prbs = []
        for _ in range(sequence_length):
            # Вычисление нового бита через обратную связь (биты 17, 3)
            new_bit = ((register >> 16) ^ (register >> 2)) & 1
            # Сдвиг регистра и добавление нового бита
            register = ((register << 1) | new_bit) & 0b1111_1111_1111_1111_1  # Обрезка до 17 бит
            prbs.append(new_bit)
        if ''.join([str(el) for el in prbs]) == subsequence:
            return i

def prbs_15(sequence_length=32782):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b1000_0000_0000_001  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 15, 1)
        new_bit = ((register >> 14) ^ (register)) & 1
        # # Вычисление нового бита через обратную связь (биты 15, 14)
        # new_bit = ((register >> 14) ^ (register >> 13)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b1111_1111_1111_111  # Обрезка до 15 бит
        prbs.append(new_bit)
    print(len(prbs))
    return prbs

def prbs_5(sequence_length=31):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b10000  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 5, 2)
        new_bit = ((register >> 4) ^ (register >> 1)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b11111  # Обрезка до 5 бит
        prbs.append(new_bit)
    
    return prbs

def prbs_32(sequence_length=4294967327):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b1000_0000_0000_0000_0000_0000_0000_0001  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 32, 28, 27, 1)
        new_bit = ((register >> 31) ^ (register >> 27) ^ (register >> 26) ^ (register)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b1111_1111_1111_1111_1111_1111_1111_1111  # Обрезка до 15 бит
        prbs.append(new_bit)
    print(len(prbs))
    return prbs

def prbs_18(sequence_length=262161):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b1000_0000_0000_0000_01  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 18, 7)
        new_bit = ((register >> 17) ^ (register >> 6)) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b1111_1111_1111_1111_11  # Обрезка до 15 бит
        prbs.append(new_bit)
    print(len(prbs))
    return prbs

def prbs_19(sequence_length=524306):
    # Инициализация регистра (seed не должен быть нулевым!)
    register = 0b1000_0000_0000_0000_001  # Пример начального состояния (может быть любым, кроме 0)
    prbs = []
    for _ in range(sequence_length):
        # Вычисление нового бита через обратную связь (биты 19, 6, 5, 1)
        new_bit = ((register >> 18) ^ (register >> 5) ^ (register >> 4) ^ register) & 1
        # Сдвиг регистра и добавление нового бита
        register = ((register << 1) | new_bit) & 0b1111_1111_1111_1111_111  # Обрезка до 15 бит
        prbs.append(new_bit)
    print(len(prbs))
    return prbs 

def prbs_new(seed, polynome, length):
    register = seed
    register_length = polynome[0]
    mask = (1 << register_length) - 1
    taps = [register_length - degree for degree in polynome]
    prbs = []
    for _ in range(length):
        new_bit = 0
        for tap in taps[1:]:
            new_bit ^= (register >> tap) & 1
        output_bit = register & 1
        prbs.append(output_bit)
        register = ((register >> 1) | (new_bit << (register_length - 1))) & mask
    return prbs

if __name__ == '__main__':
    polynome = [12, 6, 4, 1, 0]
    polynome = [12, 7, 4, 3, 0]
    polynome = [12, 11, 10, 4, 0]
    seed = 0b110101010101
    window = 12

    
    # seed = 0b10
    # polynome = [2, 1, 0]
    # window = 2

    seed = 0b100
    polynome = [3, 1, 0]
    window = 3
    
    # seed = 0b1000
    # polynome = [4, 1, 0]
    # window = 4

    # seed = 0b10000
    # polynome = [5, 2, 0]
    # window = 5

    # sequence = lfsr_Fibonacci(seed, polynome=polynome, length=35)
    sequence = prbs12()
    # sequence = prbs_new(0b110101010101, [12, 6, 4, 1], 4095)
    # sequence = prbs_new(0b10, [2, 1], 10)
    sequence = prbs_5()
    sequence = prbs_12()
    window = 12
    sequence = prbs_17()
    window = 17
    print(f'{bin(find_seed_17()) = }')
    # sequence = prbs_18()
    # window = 18
    # sequence = prbs_19()
    # window = 19
    # 00000000000000000
    # sequence = prbs_32()
    # window = 32
    # sequence = prbs_15()
    # window = 15
    print(''.join([str(el) for el in sequence]))
    test_result = test_sequence(sequence, window)
    print('Test was finished!')
    # print(test_result)