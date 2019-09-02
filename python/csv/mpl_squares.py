
import matplotlib.pyplot as plt


#数据
input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
#
plt.plot(input_value, squares, linewidth = 5)
#设置标题, 给坐标轴设置标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square_value", fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis = "both", labelsize = 14)
plt.show()



