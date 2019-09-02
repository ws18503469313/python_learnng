import numpy as np


"""
机器学习使用训练数据进行学习。
使用训练数据进行学习，
严格来说，就是针对训练数据计算损失函数的值，找出使该值尽可能小的参数
"""
"""
损失函数
"""

"""
均方误差
"""
def mean_squared_error(y, t):
    y = np.array(y)
    t = np.array(t)
    return 0.5 * np.sum((y-t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

print(str(mean_squared_error(y, t)))

"""
交叉熵误差
"""
def cross_entropy_error(y, t):
    y = np.array(y)
    t = np.array(t)
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

print(str(cross_entropy_error(y, t)))