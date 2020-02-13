
# сделал это задание не через функции, т.к. в задание этого не требовалось
answer = 0
while True:
    num = input('Если хотите выйти из программы введите "Q", иначе вводите числа')
    if num.upper() == 'Q':
        print(answer)
        break
    result = []
    i = 0
    while i < len(num):
        result.append(int(num[i] + ' '))
        i += 1
    answer += sum(result)
    print(answer)

