
class Worker:
    dic = {'wage': 5000, 'bonus': 5000}
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'Engener'
    _income = dic.get('wage')+dic.get('bonus')

class Position(Worker):
    def get_full_name(self):
        print(Worker.name + Worker.surname + Worker.position)
    def get_total_income(self):
        print(Worker._income)

res = Position()
res.get_full_name()
res.get_total_income()