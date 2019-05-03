import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Reds, edgecolors='none', s = 5)

# set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel('Square of value', fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5100, 0, 25000000])

plt.show()