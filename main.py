from lane import Lane, DeadError
from leftlane import LeftLane
from rightlane import RightLane


# read first line
nums = [int(x) for x in input().split()]
lanes = []
Lane.width = nums[1]

# read lane infos
for i in range(nums[0]):
    lane_info = [int(x) for x in input().split()]
    lanes.append(RightLane(lane_info[0], lane_info[1], lane_info[2], i) if i % 2 == 0 else
                 LeftLane(lane_info[0], lane_info[1], lane_info[2], i))

# read moves and set position
text = input().split()
x_pos = int(text[0])
y_pos = nums[0]

try:
    if text[1].count('U') < nums[0] + 1:
        raise DeadError

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
                lane.next(x_pos, y_pos)

    if y_pos != -1:
        raise DeadError

    print('safe')

except DeadError:
    print('squish')
