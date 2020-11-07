from lane import Lane, DeadError


class LeftLane(Lane):
    def __init__(self, offset, interval, speed, lane_num):
        super().__init__(Lane.width - offset - 1, -interval, -speed, lane_num)

        self.cars = range(self.first, -1, self.interval)  # position of cars

    def next(self, x_pos, y_pos):
        # check if new car is coming into view
        if self.first + self.speed - self.interval < Lane.width:
            self.first += self.speed - self.interval
        else:
            self.first += self.speed
        print(self.first)

        # if Froggie in lane
        if y_pos == self.lane_num:
            temp = self.cars
            self.cars = range(self.first, self.cars[-1] + self.speed - 1, self.interval)

            # there is a new car
            if len(temp) != len(self.cars):
                temp = list(temp)
                temp.insert(0, Lane.width)

            for init, final in zip(temp, self.cars):
                if x_pos in range(final, init) or x_pos == final:
                    raise DeadError

        else:
            self.cars = range(self.first, -1, self.interval)
            print(list(self.cars))
