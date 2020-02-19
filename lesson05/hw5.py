with open('hw5.txt', 'w') as f:
    f.writelines(['1 ', '2 ', '5 ', '79 ', '65'])
with open('hw5.txt') as f:
    for line in f:
        res = line.split(' ')
    a = 0
    for i in res:
        a = a + int(i)
    print(a)


