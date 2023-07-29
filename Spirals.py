from math import *


def archimedean_spiral(r, theta_1, step, theta_2, dis):
    points = []
    points2 = []
    degree = theta_1
    b = r
    diss = dis
    w = 1
    sign0 = 1
    i = 1
    lost = [-1, 1, 1, -1]
    while degree <= theta_2:
        t = radians(degree)
        x = b * t * cos(w * t)
        y = b * t * sin(w * t)

        dy_dphi = b * sin(w * t) + b * t * w * cos(w * t)
        dx_dphi = b * cos(w * t) - b * t * w * sin(w * t)
        dy_dx = dy_dphi / dx_dphi
        dy_dx_2 = -w*(cos(w*t)**2*t**2*w**2+3*cos(w*t)*sin(w*t)*t*w+t**2*w**2-2*cos(w*t)**2+4) /\
            (b*(-cos(w*t)**2*sin(w*t)*t**3*w**3+3*cos(w*t)**3*t**2*w**2+sin(w*t)*t**3*w**3 +
                3*cos(w*t)**2*sin(w*t)*t*w-3*cos(w*t)*t**2*w**2-cos(w*t)**3))
        alpha = atan(dy_dx)
        if alpha >= 0 and dy_dx_2 >= 0:
            theta = alpha - pi / 2
        elif alpha < 0 and dy_dx_2 < 0:
            theta = alpha + pi / 2
        elif alpha > 0 and dy_dx_2 < 0:
            theta = alpha + pi / 2
        elif alpha < 0 and dy_dx_2 > 0:
            theta = alpha - pi / 2
        xx = x + diss * cos(theta)
        yy = y + diss * sin(theta)

        # xz2 = x
        # yz2 = y
        #
        # alpha2 = atan(dy_dx)
        # sign = lambda n: copysign(1, n)
        # if sign(dy_dx) != sign0:
        #     sign0 = sign(dy_dx)
        #     i += 1
        # theta2 = alpha2 + lost[i % 4 - 1] * pi / 2
        # xzz2 = xz2 + dis * cos(theta2)
        # yzz2 = yz2 + dis * sin(theta2)

        x2 = - x + 2 * b * radians(theta_2) + dis
        y2 = - y
        xx2 = - xx + 2 * b * radians(theta_2) + dis
        yy2 = - yy

        points.append((x, y, xx, yy))
        points2.append((xx2, yy2, x2, y2))
        degree += step

    for h in reversed(points2):
        points.append(h)
    return points


def fermat_spiral(r, theta_1, step, theta_2, dis):
    # r = a * sqrt(phi) * phi
    # x = a * sqrt(phi) * cos(phi)
    # y = a * sqrt(phi) * sin(phi)
    points = []
    degree = theta_1
    while degree <= theta_2:
        t = radians(degree)
        x = r * sqrt(t) * cos(t)
        y = r * sqrt(t) * sin(t)
        xx = r * t * cos(t)
        yy = r * t * sin(t)

        points.append((x, y, xx, yy))
        degree += step
    return points
