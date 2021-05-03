def compress(data, N, M):
    from copy import deepcopy
    data = deepcopy(data)
    for i in range(N - 1, -1, -1):
        if i % 2:
            del data[i]
    data = list(zip(*data)) 
    for i in range(M - 1, -1, -1):
        if i % 2:
            del data[i]
    return list(zip(*data)) 
 
def input_data(N, M):
    print('\n[!] Заполните построчно псевдографическое изображение!\n')
    data = [] 
    for i in range(N):
        row = list(input(('[{:>%d}/{}]> ' % (len(str(N)))).format(i + 1, N)))
        length = len(row)
        if length < M: 
            row += ['.'] * (M - length) 
        else:
            row = row[:M] 
        data.append(row)
    return data
 
if '__main__' == __name__:
    N, M = [int(x) for x in input('Введите N & M через пробел: ').split()]
    data = input_data(N, M)
    data = compress(data, N, M)
    print('\nРезультат сжатия:')
    for row in data:
        print(''.join(row))