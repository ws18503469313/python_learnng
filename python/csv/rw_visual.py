
import matplotlib.pyplot as plt

from randon_walk import RandomWalk

while True :
    rw =RandomWalk()

    rw.fill_walk()
    plt.plot(rw.x_values, rw.y_values, linewidth = 2)
    plt.scatter(0, 0, edgecolors = "none", s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = "red", edgecolors = "none", s = 100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    another = input("another?(y/n):")
    if another == 'n' :
        break
