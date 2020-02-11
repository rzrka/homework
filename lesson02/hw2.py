user = input('введите число')
mass = []
i = 0

while i < len(user):
    mass.append(user[i])
    i += 1
for n in range(0, len(mass), 2):
    mass[n - 1], mass[n] = mass[n], mass[n - 1]




print(mass)