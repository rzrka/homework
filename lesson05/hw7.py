import json
with open('hw7.txt') as f:
    res = []
    profit_firm = 0
    global_dic = {}
    def my_func(firm):
        my_items = []
        income = int(firm[2]) - int(firm[3])
        for line in firm:
            res = line.split(' ')
            if res != ['ООО']:
                my_items.append(res)
        global_dic.update({firm[0]: income})
        return income



    firm = f.readline().split(' ')
    if my_func(firm) > 0:
        profit_firm = profit_firm + my_func(firm)

    firm = f.readline().split(' ')
    if my_func(firm) > 0:
        profit_firm = profit_firm + my_func(firm)

    firm = f.readline().split(' ')
    if my_func(firm) > 0:
        profit_firm = profit_firm + my_func(firm)

    res.append(global_dic)
    res.append({'average_profit': profit_firm / len(global_dic)})

with open('my_file.json', 'w') as f:
    json.dump(res, f)






            

