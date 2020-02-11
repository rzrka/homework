#через словарь
user = int(input('Введите месяц'))
season_dic = {
    (12, 1, 2): 'Зима',
    (3, 4, 5): 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень'
}

for key in season_dic:
    if user == 12 or user == 1 or user == 2:
        print('Зима')
        break
    elif user == 3 or user == 4 or user == 5:
        print('Весна')
        break
    elif user == 6 or user == 7 or user == 8:
        print('Лето')
        break
    else:
        print('Осень')
        break

#сделал через списки, хотя как по мне это было не обязательно так как,
# я использовал списки когда делал через словарь
season_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for key in season_list:
    if user == 12 or user == 1 or user == 2:
        print('Зима')
        break
    elif user == 3 or user == 4 or user == 5:
        print('Весна')
        break
    elif user == 6 or user == 7 or user == 8:
        print('Лето')
        break
    else:
        print('Осень')
        break

