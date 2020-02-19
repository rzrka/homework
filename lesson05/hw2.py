with open('hw2.txt', 'r') as f:
    print('Количество строк: ', len(f.readlines()))
    f.seek(0)
    for line in f:
        print('Количество букв в слово: ', len(line))
