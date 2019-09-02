import numpy as np
import matplotlib.pylab as plt

def step_fun(x):
    return  np.array(x > 0, dtype = np.int)


# x = np.arange(-5.0, 5.0, 0.1)
#
# y = step_fun(x)
#
# plt.plot(x, y)
#
# plt.ylim(-0.1, 1.1)
#
# plt.show()
def sigmoid(x):
    return  1 / (1 + np.exp(-x))

# x = np.array([-1, 1, 2.0])

# print(sigmoid(x))

# t = np.array([1, 2, 3])
#
# print(1 + t)
#
# print(1 / t)

x = np.arange(-5, 5, 0.1)

y = sigmoid(x)



