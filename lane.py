from abc import ABC, abstractmethod


class DeadError(Exception):
    pass


class Lane(ABC):
    # width of the board (static var)
    width = 0

    def __init__(self, first, interval, speed, lane_num):
        self.first = first
        self.interval = interval
        self.speed = speed
        self.lane_num = lane_num
        self.cars = None

    @abstractmethod
    def next(self, x_pos, y_pos):
        pass

    def display(self):
        for j in range(Lane.width):
            print('0' if j not in self.cars else '1', end=' ')
        print()
