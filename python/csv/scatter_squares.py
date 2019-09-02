
import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)

plt.title("Square Nums", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square_value", fontsize = 14)

plt.tick_params(axis = "both", which="major", labelsize = 14)


x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 4, 9, 16, 25]
#plt.scatter(x_vals, y_vals, c = "red",  edgecolor = 'none',  s = 40)
plt.scatter(x_vals, y_vals, c = y_vals, cmap = plt.cm.Blues,  edgecolor = 'none',  s = 40)

plt.show()

plt.savefig("saved.png", bbox_inches = "tight")



