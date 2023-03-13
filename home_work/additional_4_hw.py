class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return "Автомобиль заведен"


    def stop(self):
        return "Автомобиль заглушен"


    def manufacture(self):
        return "Автомобиль - {}".format(self.year)

    def model(self):
        return "Автомобиль - {}".format(self.type)

    def outer(self):
        return "Автомобиль - {}".format(self.color)

car1 = Car('blue ', 'Rav4 ', '2021')
print(car1.start())
print(car1.stop())
print(car1.manufacture())
print(car1.model())
print(car1.outer())




