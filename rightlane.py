from lane import Lane, DeadError


class RightLane(Lane):
    def __init__(self, first, interval, speed, lane_num):
        self.first = first
        self.interval = interval
        self.speed = speed
        self.incoming_car = interval - speed
        self.lane_num = lane_num
        self.cars = range(first, Lane.width, interval)  # position of cars

    def next(self, x_pos, y_pos):
        # check if new car is coming into view
        if self.first >= self.incoming_car:
            self.first -= self.incoming_car
        else:
            self.first += self.speed

        # if Froggie in lane
        if y_pos == self.lane_num:
            temp = self.cars
            self.cars = range(self.first, self.cars[-1] + self.speed + 1, self.interval)

            # there is a new car
            if self.first != temp[0]:
                temp = list(temp)
                temp.insert(0, -1)

            for init, final in zip(temp, self.cars):
                if x_pos in range(final, init, -1) or x_pos == final:
                    raise DeadError

        else:
            self.cars = range(self.first, Lane.width, self.interval)
