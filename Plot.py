from math import *
import matplotlib.pyplot as plt


def plot_coord(nodes, head, dis):
    # plt.style.use('Solarize_Light2')
    inner = [c for c in nodes[0]]
    outer = [c for c in nodes[1]]
    x_inner = [c[0] for c in inner]
    y_inner = [c[1] for c in inner]
    x_outer = [c[0] for c in outer]
    y_outer = [c[1] for c in outer]
    plt.plot(x_inner, y_inner, label=f"inner_{dis}")
    plt.plot(x_outer, y_outer, label=f"outer_{dis}")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.legend(loc='upper left')
    plt.title(f'{head} spiral')
    plt.grid()
    plt.axis('equal')
    plt.show()
