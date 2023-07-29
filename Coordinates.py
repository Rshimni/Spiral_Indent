from math import *


def edit(coord):
    g = coord
    g.reverse()
    sign = lambda x: copysign(1, x)
    for i in range(1, len(coord)):
        if sign(g[i][1]) == sign(g[i-1][1]):
            d = 1
        else:
            q = i
            break
    return q


def spiral_nodes(nodes, dis, b):
    x_1 = nodes[0]
    y_1 = nodes[1]

    x_2 = nodes[2]
    y_2 = nodes[3]


    coord_1 = []
    coord_2 = []
    for j in range(len(x_1)):
        coord_1.append((x_1[j], y_1[j]))
    for k in range(len(x_2)):
        coord_2.append((x_2[k], y_2[k]))
    pon = coord_1#[edit(coord=coord_1)::]
    nop = coord_2#[edit(coord=coord_2)::]
    x_i_1 = [c[0] for c in pon]
    y_i_1 = [c[1] for c in pon]
    x_o_1 = [c[0] for c in nop]
    y_o_1 = [c[1] for c in nop]

    # x_i_2 = [-c[0] + 19.085 for c in pon]
    # y_i_2 = [-c[1] for c in pon]
    # x_o_2 = [-c[0] + 19.085 for c in nop]
    # y_o_2 = [-c[1] for c in nop]
    # x_i_1.reverse()
    # y_i_1.reverse()
    # x_o_1.reverse()
    # y_o_1.reverse()
    x_final_main = x_i_1
    y_final_main = y_i_1
    x_final_offset = x_o_1
    y_final_offset = y_o_1

    # for i in x_o_2:
    #     x_final_main.append(i)
    # for i in y_o_2:
    #     y_final_main.append(i)
    # for i in x_i_2:
    #     x_final_offset.append(i)
    # for i in y_i_2:
    #     y_final_offset.append(i)

    final_coordinates_spiral_main = []
    for i in range(len(x_final_main)):
        final_coordinates_spiral_main.append((x_final_main[i], y_final_main[i]))
    final_coordinates_spiral_offset = []
    for i in range(len(x_final_offset)):
        final_coordinates_spiral_offset.append((x_final_offset[i], y_final_offset[i]))
    return [final_coordinates_spiral_main, final_coordinates_spiral_offset]

