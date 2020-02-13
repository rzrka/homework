def my_func(num):
    value_1 =max(num)
    num.remove(max(num))
    value_2 = max(num)
    num.remove(max(num))
    print(value_1+value_2)

a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
my_list = [a, b ,c]
my_func(my_list)





