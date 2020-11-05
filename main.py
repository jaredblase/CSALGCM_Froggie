class Lane:
    # width of the board (static var)
    width = 0

    def __init__(self, lane_num, first, interval, speed):
        self.lane_num = lane_num
        self.first = first
        self.interval = interval
        self.speed = speed
        if lane_num % 2 == 0:
            self.basis = Lane.width
        else:
            self.basis = -1

        self.cars = range(first, self.basis, interval)

    def next(self):
        # if there is a new car coming
        if self.first >= self.interval - self.speed:
            self.first += self.speed - self.interval
        else:
            self.first += self.speed

        # if Froggie not in lane
        if y_pos != self.lane_num:
            self.cars = range(self.first, self.basis, self.interval)
        else:
            temp = self.cars
            self.cars = range(self.first, self.basis, self.interval)

            for init, final in zip(temp, self.cars):
                if x_pos in range(final, init, -1):
                    raise Exception

    def display(self):
        for j in range(Lane.width):
            print('0' if j not in self.cars else '1', end=' ')
        print()


# read first line
nums = [int(x) for x in input().split()]
lanes = []
Lane.width = nums[1]

# read lane infos
for i in range(nums[0]):
    lane_info = [int(x) for x in input().split()]
    if i % 2 == 0:
        lanes.append(Lane(i, lane_info[0], lane_info[1], lane_info[2]))
    else:
        lanes.append(Lane(i, Lane.width - 1 - lane_info[0], -lane_info[1], -lane_info[2]))


# read moves and set position
text = input().split()
x_pos = int(text[0])
y_pos = nums[0]

try:
    if text[1].count('U') < nums[0] + 1:
        raise Exception

    for move in text[1]:
        if move == 'L':
            x_pos = (x_pos - 1) % Lane.width
        elif move == 'R':
            x_pos = (x_pos + 1) % Lane.width
        else:
            y_pos += -1 if move == 'U' else 1

        # not reached end of line
        if y_pos != -1:
            for lane in lanes:
                lane.display()
                lane.next()
            print()

    print('safe')

except:
    print('squish')
