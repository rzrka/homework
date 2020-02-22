
class Road:
    def __init__(self, length, width):
        self.calc = length * width * 25 * 5
        self._length = length
        self._width = width

res = Road(10, 50)
print(res.calc)
