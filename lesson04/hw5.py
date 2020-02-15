import functools
def my_func(x, y):
    return x * y
num = [el for el in range(100,1001) if el % 2 == 0]



print(functools.reduce(my_func, num))