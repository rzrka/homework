def my_func(x, y):
    i = 0
    res = 1
    while i < y*(-1):
        res = 1/x*res
        i += 1
    print(res)

x = int(input('Введите число'))
y = int(input('введите степень'))*-1
my_func(x, y)



