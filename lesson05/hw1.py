with open('hw1.txt', 'w') as f:
    user = 1
    res = []
    while user != '':
        user = input('Введите слово')
        res.append(user)
    
    for line in res:
        f.write(line + '\n')




