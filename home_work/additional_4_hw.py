class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return "Автомобиль заведен"


    def stop(self):
        return "Автомобиль заглушен"


    def manufacture(self, year_new):
        self.year = year_new


    def model(self, type_new):
        self.type = type_new


    def outer(self, color_new):
        self.color = color_new


car1 = Car('blue ', 'Rav4 ', '2021')
print(car1.start())
print(car1.stop())





