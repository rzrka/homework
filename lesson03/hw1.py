
def my_func(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = 0
    print(c)

a = int(input('Введите число'))
b = int(input('Введите число'))
my_func(a ,b)



