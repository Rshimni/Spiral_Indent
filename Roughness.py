from math import *
from Measure import *


def slope(coord):
    x = [c[0] for c in coord[0]]
    y = [c[1] for c in coord[0]]
    xx = [c[0] for c in coord[1]]
    yy = [c[1] for c in coord[1]]
    # xx2 = [c[0] for c in coord[2]]
    # yy2 = [c[1] for c in coord[2]]
    rad = []
    for i in range(1, len(x)):
        p = y[i] - y[i - 1]
        q = x[i] - x[i - 1]
        m = p / q
        if p > 0 and q < 0:
            rad.append(pi - abs(atan(m)))
        elif p < 0 and q < 0:
            rad.append(pi + abs(atan(m)))
        else:
            rad.append(atan(m))
    rad2 = []
    for i in range(1, len(xx)):
        p = yy[i] - yy[i - 1]
        q = xx[i] - xx[i - 1]
        m = p / q
        if p > 0 and q < 0:
            rad2.append(pi - abs(atan(m)))
        elif p < 0 and q < 0:
            rad2.append(pi + abs(atan(m)))
        else:
            rad2.append(atan(m))
    # rad3 = []
    # for i in range(1, len(xx2)):
    #     p = yy2[i] - yy2[i - 1]
    #     q = xx2[i] - xx2[i - 1]
    #     m = p / q
    #     if p > 0 and q < 0:
    #         rad3.append(pi - abs(atan(m)))
    #     elif p < 0 and q < 0:
    #         rad3.append(pi + abs(atan(m)))
    #     else:
    #         rad3.append(atan(m))
    return [rad, rad2]


#######################################################################################################################
#######################################################################################################################
def rotate(delta, amp, coord):
    x = [c[0] for c in coord[0]]
    y = [c[1] for c in coord[0]]
    xx = [c[0] for c in coord[1]]
    yy = [c[1] for c in coord[1]]
    # xx2 = [c[0] for c in coord[2]]
    # yy2 = [c[1] for c in coord[2]]
    phi = delta[0]
    alpha = delta[1]
    # beta = delta[2]
    long_1 = []
    for q in range(1, len(x)):
        long_1.append(distance(x[q - 1], y[q - 1], x[q], y[q]))
    long_2 = []
    for q in range(1, len(xx)):
        long_2.append(distance(xx[q - 1], yy[q - 1], xx[q], yy[q]))
    # long_3 = []
    # for q in range(1, len(xx2)):
    #     long_3.append(distance(xx2[q - 1], yy2[q - 1], xx2[q], yy2[q]))

    start_x = x[0]
    start_y = y[0]
    start_xx = xx[0]
    start_yy = yy[0]
    # start_xx2 = xx2[0]
    # start_yy2 = yy2[0]
    xy_coordinate = {}
    xxyy_coordinate = {}
    # xxyy2_coordinate = {}
    x1_data = []
    y1_data = []
    xx1_data = []
    yy1_data = []
    # xx2_data = []
    # yy2_data = []
    for i in range(len(phi)):
        j = 0
        while j <= long_1[i]:
            u = j
            v = amp * sin(j * 2 * pi / long_1[i])
            x = cos(phi[i]) * u - sin(phi[i]) * v + start_x
            y = sin(phi[i]) * u + cos(phi[i]) * v + start_y
            x1_data.append(x)
            y1_data.append(y)
            j += 0.04
        xy_coordinate.update({i: [x1_data, y1_data]})
        start_x = x
        start_y = y
        x1_data = []
        y1_data = []

    for w in range(len(alpha)):
        k = 0
        while k <= long_2[w]:
            uu = k
            vv = amp * sin(k * 2 * pi / long_2[w])
            xx = cos(alpha[w]) * uu - sin(alpha[w]) * vv + start_xx
            yy = sin(alpha[w]) * uu + cos(alpha[w]) * vv + start_yy
            xx1_data.append(xx)
            yy1_data.append(yy)
            k += 0.04
        xxyy_coordinate.update({w: [xx1_data, yy1_data]})
        start_xx = xx
        start_yy = yy
        xx1_data = []
        yy1_data = []

    # for w in range(len(beta)):
    #     k = 0
    #     while k <= long_3[w]:
    #         uu = k
    #         vv = -amp * sin(k * 2 * pi / long_3[w])
    #         xx2 = cos(beta[w]) * uu - sin(beta[w]) * vv + start_xx2
    #         yy2 = sin(beta[w]) * uu + cos(beta[w]) * vv + start_yy2
    #         xx2_data.append(xx2)
    #         yy2_data.append(yy2)
    #         k += 0.02
    #     xxyy2_coordinate.update({w: [xx2_data, yy2_data]})
    #     start_xx2 = xx2
    #     start_yy2 = yy2
    #     xx2_data = []
    #     yy2_data = []

    final_x_data = []
    final_y_data = []
    for k in range(len(xy_coordinate)):
        x_c = xy_coordinate[k][0][:]
        y_c = xy_coordinate[k][1][:]
        for j in range(len(x_c)):
            final_x_data.append(x_c[j])
            final_y_data.append(y_c[j])

    final_xx_data = []
    final_yy_data = []
    for k in range(len(xxyy_coordinate)):
        xx_c = xxyy_coordinate[k][0][:]
        yy_c = xxyy_coordinate[k][1][:]
        for j in range(len(xx_c)):
            final_xx_data.append(xx_c[j])
            final_yy_data.append(yy_c[j])

    # final_xx2_data = []
    # final_yy2_data = []
    # for k in range(len(xxyy2_coordinate)):
    #     xx_c = xxyy2_coordinate[k][0][:]
    #     yy_c = xxyy2_coordinate[k][1][:]
    #     for j in range(len(xx_c)):
    #         final_xx2_data.append(xx_c[j])
    #         final_yy2_data.append(yy_c[j])
    return [final_x_data, final_y_data, final_xx_data, final_yy_data]
