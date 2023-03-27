import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# RGB colour must be between 0-1. 0= darker, 1= lighter.
# line colour ex.c='red', c=(0.12, 0.22, 0.74).

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5, c=y_values, cmap=plt.cm.Reds)


# Set chart title and label axis.
ax.set_title("Square Numbers.", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set the size of the tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()