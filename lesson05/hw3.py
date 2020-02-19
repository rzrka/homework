with open('hw3.txt', 'r') as f:
    res = f.readlines()
    avg = 0
    my_list = [el.split(' ')[:-1] for el in res]
    for i in my_list:
        avg = avg + int(i[1])
        if int(i[1]) < 20:
            print(i[0])
    print('Средний доход', avg / len(res))











