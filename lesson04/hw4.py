my_list = (1, 2, 5, 5, 70, 70, 76, 3, 5, 4)
new_list = [el for el in my_list if my_list.count(el) <= 1]
print(new_list)



