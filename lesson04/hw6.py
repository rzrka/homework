from itertools import count, cycle

for el in count(1):
    print(el)

for el2 in cycle('abc'):
    print(el2)