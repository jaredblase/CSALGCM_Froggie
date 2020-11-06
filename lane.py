from abc import ABC, abstractmethod


class DeadError(Exception):
    pass


class Lane(ABC):
    # width of the board (static var)
    width = 0

    @abstractmethod
    def next(self, x_pos, y_pos):
        pass

    def display(self):
        for j in range(Lane.width):
            print('0' if j not in self.cars else '1', end=' ')
        print()
