
class Car:
    speed = 60
    color = 'черная'
    name = 'приора'
    is_police = True

    def show_car(self):
        if Car.is_police is True:
            example = 'Машина полицейского типа'
        else:
            example = 'Машина гражданского типа'
        print('{} {} {}'.format(Car.color, Car.name, example))

    def move(self, go, turn, stop):
        print('Автомобиль проехал')
        self.go = go
        self.turn = turn
        self.stop = stop

    def show_speed(self):
        print('автомобиль ехать со скоростью: ', Car.speed)

class TownCar(Car):

     def show_speed(self):
        if Car.speed > 60:
            print('Превышение скорости')
        else:
            print('автомобиль ехать со скоростью: ', Car.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if Car.speed > 40:
            print('Превышение скорости')
        else:
            print('автомобиль ехать со скоростью: ', Car.speed)
    pass
class PoliceCar(Car):
    pass



town_car = TownCar()
town_car.show_car()
town_car.move('прямо', 'налево', 'остановился')
print('{} {} {}'.format(town_car.go, town_car.turn, town_car.stop))
town_car.show_speed()

sport_car = SportCar()
sport_car.show_car()
sport_car.move('прямо', 'налево', 'остановился')
print('{} {} {}'.format(sport_car.go, sport_car.turn, sport_car.stop))
sport_car.show_speed()

work_car = WorkCar()
work_car.show_car()
work_car.move('прямо', 'налево', 'остановился')
print('{} {} {}'.format(work_car.go, work_car.turn, work_car.stop))
work_car.show_speed()

police_car = PoliceCar()
police_car.show_car()
police_car.move('прямо', 'налево', 'остановился')
print('{} {} {}'.format(police_car.go, police_car.turn, police_car.stop))
police_car.show_speed()
