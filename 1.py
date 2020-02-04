import time


class TrafficLight:
    dict = {"красный": "41", "желтый": "43", "зеленый": "42"}

    def running(self, color):
        time1 = int(time.time())
        if (color != "красный" or color != "желтый" or color != "зеленый"):
            color = "красный"
        self.__color = color
        time1 = int(time.time())
        i = 0
        fl = color
        print(f"\033[30m\033[{str(self.dict[fl])}m {self.__color}")
        while i < 10:

            time2 = int(time.time())
            if (time2 - time1 == 7 and (self.__color == "красный" or self.__color == "зеленый")) or (
                    time2 - time1 == 2 and self.__color == "желтый"):
                i += 1
                time1 = time2
                if (self.__color == "красный") or (self.__color == "зеленый"):
                    fl = self.__color
                    self.__color = "желтый"
                    print(f"\033[30m\033[43m {self.__color}")

                else:
                    if fl == "красный":
                        fl = "зеленый"
                    else:
                        fl = "красный"
                    print(f"\033[30m\033[{str(self.dict[fl])}m {fl}")
                    self.__color = fl


new = TrafficLight()
new.running("красный")  # красный, желтый или зеленый
