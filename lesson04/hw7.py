user = int(input('Введите число'))
while user >= 15:
    user = int(input('Введите число меньше или ровно 15: '))

my_fibo = range(1, user + 1)

res = 1
def fibo_gen():
    for el in my_fibo:
        yield el

for el in fibo_gen():
    res = el * res

print(res)