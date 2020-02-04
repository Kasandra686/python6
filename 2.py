class Road :
    def __init__(self,length,width):
        self._length=length
        self._width=width
    def calculate(self):
        return (self._width*self._length*25*5/1000)


new = Road(5000,20)
print(new.calculate())