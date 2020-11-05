class Lane:
    # width of the board (static var)
    width = 0

    def __init__(self, first, interval, speed):
        self.first = first
        self.interval = interval
        self.speed = speed

        self.lane_num = i
        self.end = end + interval
        self.cars = range(first, end, interval)  # position of cars

    def next(self):
        # if there is a new car coming
        if self.interval > 0:
            if self.first >= self.interval - self.speed:
                self.first += self.speed - self.interval
            else:
                self.first += self.speed
        else:
            if self.first + self.speed - self.interval < Lane.width:
                self.first += self.speed - self.interval
            else:
                self.first += self.speed

        # if Froggie in lane
        # I don't really know now

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
        end = Lane.width
        lanes.append(Lane(lane_info[0], lane_info[1], lane_info[2]))
    else:
        end = -1
        lanes.append(Lane(Lane.width - 1 - lane_info[0], -lane_info[1], -lane_info[2]))

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

        # if end reached
        if y_pos == -1:
            break
        else:
            for lane in lanes:
                lane.next()

    if y_pos != -1:
        raise Exception

    print('safe')

except:
    print('squish')
