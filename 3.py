class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        print(self._Worker__income["wage"] + self._Worker__income["bonus"])


new = Position("Игорь", "Иванов", "электрик", 2000, 4000)
new.get_full_name()
new.get_total_income()
