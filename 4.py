class Car :
    def __init__(self,speed, color , name):
        speed=speed
        color=color
        name=name
        is_police=False
    def go(self):
        pass
    def stop(self):
        pass
    def turn(self, direction ):
        pass

class TownCar(Car):
    def show_speed(self):
        print("скорость1")
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print("скорость2")
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

new = WorkCar(50,"red","dasa")
# не работает. не понятное задание, а потому не интересное(( пару часов потрачено на попытку понять задание