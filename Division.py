from math import *
from Measure import *


def segmentation(divide, length, points):
    segment = length[0] / divide
    divide2 = floor(length[1] * divide / length[0])
    # divide3 = floor(length[2] * divide / length[0])
    segment2 = length[1] / divide2
    # segment3 = length[2] / divide3
    print(f"segment1: {segment}--segment2: {segment2}")
    x_data = [c[0] for c in points]
    y_data = [c[1] for c in points]
    xx_data = [c[2] for c in points]
    xx_data.insert(0, x_data[0])
    yy_data = [c[3] for c in points]
    yy_data.insert(0, y_data[0])
    # xx2_data = [c[6] for c in points]
    # yy2_data = [c[7] for c in points]
    coordinate = [(x_data[0], y_data[0])]
    coordinate2 = [(xx_data[0], yy_data[0])]
    # coordinate3 = [(xx2_data[0], yy2_data[0])]
    n = 0
    for _ in range(divide):
        span = 0
        for i in range(n + 1, len(x_data)):
            span += distance(x_data[i - 1], y_data[i - 1], x_data[i], y_data[i])
            if span > segment:
                coordinate.append((x_data[i], y_data[i]))
                n = i
                break

    n = 0
    for _ in range(divide2):
        span = 0
        for i in range(n + 1, len(xx_data)):
            span += distance(xx_data[i - 1], yy_data[i - 1], xx_data[i], yy_data[i])
            if span > segment2:
                coordinate2.append((xx_data[i], yy_data[i]))
                n = i
                break
    # n = 0
    # for _ in range(divide3):
    #     span = 0
    #     for i in range(n + 1, len(xx2_data)):
    #         span += distance(xx2_data[i - 1], yy2_data[i - 1], xx2_data[i], yy2_data[i])
    #         if span > segment3:
    #             coordinate3.append((xx2_data[i], yy2_data[i]))
    #             n = i
    #             break
    # coordinate2.append(coordinate[-1])
    return [coordinate, coordinate2]
