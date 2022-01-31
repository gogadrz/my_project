import math


class Automobile:

    def __init__(self, x, y, angle, vehicle_type='Машина'):
        self.__x = x
        self.__y = y
        self.__angle = angle
        self.__odometer = 0
        self.__vehicle_type = vehicle_type

    def turn(self, angle):
        self.__angle = angle

    def move(self, distance):
        self.__odometer += distance
        self.__x = self.__x + distance * math.cos(math.radians(self.__angle))
        self.__y = self.__y + distance * math.sin(math.radians(self.__angle))

    def get_odometer(self):
        return self.__odometer

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_angle(self):
        return self.__angle

    def info(self, new_line=True):
        print('{vehicle}:\nКоординаты. x: {x}, y: {y}\n'
              'Угол: {angle} градусов\n'              
              'Пройденное расстояние: {dist} км'.format(
                                                        vehicle=self.__vehicle_type,
                                                        x=round(self.get_x(), 2),
                                                        y=round(self.get_y(), 2),
                                                        angle=self.get_angle(),
                                                        dist=self.get_odometer())
        )

        if new_line:
            print()


class Bus(Automobile):
    __ticket_cost = 10

    def __init__(self, x, y, angle, vehicle_type='Автобус'):
        super().__init__(x, y, angle, vehicle_type)
        self.__passenger_count = 0
        self.__revenue = 0

    def get_on_the_bus(self, passengers):
        self.__passenger_count += passengers

    def get_off_the_bus(self, passengers):
        self.__passenger_count -= passengers

    def move(self, distance):
        self.__revenue += distance * self.__ticket_cost * self.__passenger_count
        super(Bus, self).move(distance)

    def info(self, new_line=True):
        super(Bus, self).info(False)
        print('Количество пассажиров: {pass_cnt} чел.\n'
              'Выручка: {revenue} рублей'.format(
                                                pass_cnt=self.__passenger_count,
                                                revenue=self.__revenue)
        )

        if new_line:
            print()


car = Automobile(15, 15, 90)
car.info()

car.move(20)
car.turn(120)
car.move(30)
car.info()

bus = Bus(0, 0, 45)

bus.move(12)
bus.info()

bus.turn(90)
bus.get_on_the_bus(25)
bus.move(10)
bus.info()

bus.get_off_the_bus(8)
bus.move(7.5)
bus.info()
