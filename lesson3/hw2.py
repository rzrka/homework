def my_func(**kwargs):
    return kwargs

name = input('Введит ваше имя')
surname = input('Введите вашу фамилию')
year = int(input('Введите год рожждения'))
town = input('введите город')
email = input('Введите почту')
num = input('Введите номер телефона')
print(my_func(имя = name, фамилия = surname, год = year, город = town, почта = email, номер = num))
