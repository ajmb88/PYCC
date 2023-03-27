import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks as long as the program is running.
while True:

    # Make a random walk.
    rw = RandomWalk(50000)
    rw.fill_walk() 

    # Plot the point in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    # Setting up the colourmap.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
                cmap=plt.cm.Reds, edgecolors='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=40)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Keep walking? y/n? :")
    if keep_running == 'n':
        break