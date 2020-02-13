def int_func(res):
    if res.find(' ') > 0:
        return (res.title())
    return res.lower()

print(int_func(input('введите слово')))




