import time
class TrafficLight:

    _red = 'красный'
    _green = 'зеленый'
    _yellow = 'желтый'
    def running(self):
        print('Запуск')
        while True:
            print(TrafficLight._red)
            time.sleep(7)
            print(TrafficLight._yellow)
            time.sleep(2)
            print(TrafficLight._green)
            time.sleep(5)


traffic_lights = TrafficLight()
traffic_lights.running()

