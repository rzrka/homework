with open('hw6.txt') as f:

    global_dict = {}
    def my_func(my_list):
        my_items = []
        dic = {}
        count_hour = 0
        for line in my_list:
            res = line.split('(')[0]
            if res != '-':
                my_items.append(res)
        for i in my_items[1:]:
            count_hour = count_hour + int(i)
        dic.update({my_items[0]: count_hour})
        global_dict.update({my_items[0]: count_hour})


    my_list = f.readline().split(' ')
    my_func(my_list)

    my_list = f.readline().split(' ')
    my_func(my_list)

    my_list = f.readline().split(' ')
    my_func(my_list)
    print(global_dict)









