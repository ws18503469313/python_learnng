import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import  imread

a = np.array([[1,2], [0,4]])

b = np.array([2,3])

print(a * b)

print(a[0])

line = np.arange(0, 6, 0.1)

y = np.sin(line)

y2 = np.cos(line)

plt.plot(line, y, label = "sin")

plt.plot(line, y2, label = "cos", linestyle = "--")

plt.xlabel("x")

plt.ylabel("y")

plt.title("sin-cos")

plt.legend()##显示符号


# img = imread('test.png')

# plt.imshow(img)
plt.show()


