user = input('Введите слова')
user = user.split()
mass = []
for n in user:
    if len(n) > 10:
        mass.append(n[0:10])
    else:
        mass.append(n)
print(mass)