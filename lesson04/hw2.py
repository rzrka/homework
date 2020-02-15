


res = []
my_list = [7, 3, 5, 8, 1, 2, 7, 8, 3, 2, 7, 10]
i = -2
new_list = (el for el in my_list)
for k in new_list:

    i += 1
    if k > my_list[i]:
        res.append(k)

print(res)

# второй вариант решения
my_list = [7, 3, 5, 8, 1, 2, 7, 8, 3, 2, 7, 10]
new_list = [el for el in my_list if el > my_list[0]]
print(new_list)

