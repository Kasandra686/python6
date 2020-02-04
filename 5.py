class Stationery:
    def __init__(self, name):
        title=name
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
     print("Запуск отрисовки ручки")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандаша")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркера")

pen = Pen("Имя")
pen.draw()
pen2 = Pencil("Имя")
pen2.draw()
pen3 = Handle("Имя")
pen3.draw()