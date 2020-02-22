class Stationery:
    title = 'аниме'
    def draw(self):
        print('запуск отрисовки')
        pass
class Pen(Stationery):
    def draw(self):
        print('запуск отрисовки')
        print('отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('запуск отрисовки')
        print('отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('запуск отрисовки')
        print('отрисовка маркером')

pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()