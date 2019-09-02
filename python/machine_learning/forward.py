import numpy as np



# 激活函数
def sigmoid(x):
    return  1 / (1 + np.exp(-x))


"""
关于输出函数

机器学习的问题大致可以分为分类问题和回归问题。
分类问题是数据属于哪一个类别的问题。
[回归问题用恒等函数] ============> 将输入按原样输出
比如，区分图像中的人是男性还是女性的问题就是分类问题。
而回归问题是根据某个输入预测一个（连续的）数值的问题。
[问题用 softmax 函数]
比如，根据一个人的图像预测这个人的体重的问题就是回归问题（类似“57.4kg”这样的预测）
"""
#
def identity_function(x):
    return x

# softmax 函数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    '''
    sofmax 的总和恒为1, 因此可以看作各个数值出现的概率
    '''
    print("========================sofmax 的总和:" + str(np.sum(y)))
    return y

# 初始化权重,偏置
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])

    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])

    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

# 神经元素处理输入
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y1 = forward(network, x)
print(y1) # [ 0.31682708 0.69627909]
y2 = softmax(y1)

print(y2)
