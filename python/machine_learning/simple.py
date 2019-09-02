import numpy as np

def AND0(x1, x2):
    w1, w2, threa = 0.5, 0.5, 0.7
    tmp = x1* w1 + x2* w2
    if(tmp <=  threa):
        return 0
    else:
        return 1

# x = np.array([0, 1])
#
# w = np.array([0.5, 0.5])
#
# b = -0.7
#
# print(w*x)
#
# print(np.sum(w*x))
#
# print(np.sum(w*x) +b)
#与门
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    temp = np.sum(w*x) + b
    #阶跃函数
    if(temp <=  0):
        return 0
    else:
        return 1
#与非门
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    temp = np.sum(w*x) + b
    #阶跃函数
    if(temp <=  0):
        return 0
    else:
        return 1
#火门
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(w*x) + b
    #阶跃函数
    if(temp <=  0):
        return 0
    else:
        return 1

#异或门
def XOR(x1, x2):
    s1 = AND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

