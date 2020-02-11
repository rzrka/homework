my_list = [7, 5, 3, 3, 2]
user = int(input('Введите число'))




for n in my_list:
    if n == user:
        my_list.insert(my_list.index(n), user)
        break
    elif user > n:
        my_list.insert(0, user)
        break
    elif user < my_list[(len(my_list) - 1)]:
        my_list.append(user)
        break







print(my_list)