import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax =plt.subplots()

x_values = [1,2,3,4,5]
y_values =[1,8,27,64,123]

# Setting the type of plot and information in it.
# Also setting colour if you choose.
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s=25)

# Set the title and labels for the graph.
ax.set_title("Cube Values", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cube of Values", fontsize = 14)

# set the tick parameters.
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()