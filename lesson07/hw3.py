class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print(self.num + other)

    def __sub__(self, other):
        print(self.num - other)

    def __mul__(self, other):
        print(self.num * other)

    def __truediv__(self, other):
        print(self.num / other)

    def make_order(self):
        pass

cell = Cell(12)
cell + 2
cell - 2
cell * 2
cell / 2



