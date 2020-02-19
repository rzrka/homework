with open('hw4.txt', 'r+', encoding='utf-8') as f:
    content = f.readlines()
    my_list = []
    dic = {'One ': 'Один', 'Two ': 'Два', 'Three ': 'Три', 'Four ': 'Четыре'}
    for line in content:
        trans = (line.split('-'))
        trans[0] = dic.get(trans[0])
        a = ' -'.join(trans)
        my_list.append(a)

    res = open('hw4.1.txt', 'r+', encoding='utf-8')
    res.writelines(my_list)
    res.close()












