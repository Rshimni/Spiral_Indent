from math import *


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


#######################################################################################################################
#######################################################################################################################
def total_length(value):
    x0 = 0
    y0 = 0
    xx0 = 0
    yy0 = 0
    xx02 = 0
    yy02 = 0
    d = 0
    dd = 0
    dd2 = 0
    x_coord = [c[0] for c in value]
    y_coord = [c[1] for c in value]
    x2_coord = [c[2] for c in value]
    y2_coord = [c[3] for c in value]
    # x3_coord = [c[6] for c in value]
    # y3_coord = [c[7] for c in value]
    for i in range(len(x_coord)):
        x = x_coord[i]
        y = y_coord[i]
        xx = x2_coord[i]
        yy = y2_coord[i]
        # xx2 = x3_coord[i]
        # yy2 = y3_coord[i]
        d += distance(x0, y0, x, y)
        dd += distance(xx0, yy0, xx, yy)
        # dd2 += distance(xx02, yy02, xx2, yy2)
        x0 = x
        y0 = y
        xx0 = xx
        yy0 = yy
        # xx02 = xx2
        # yy02 = yy2
    return [d, dd]
