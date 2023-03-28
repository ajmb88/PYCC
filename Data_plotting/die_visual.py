from die import Die

# Create a D6
from plotly.graph_objs import Bar, Layout
from plotly import offline


die = Die()

# Make some rolls and store the results in a list, then display results.
results = []
for roll in range(10000):
    result = die.roll()
    results.append(result)


# analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


print(frequencies)

# Visualize the results.
x_value = list(range(1, die.num_sides+1))
data = (Bar(x = x_value, y = frequencies))

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency or Results'}
my_layout = Layout(title="Results of rolling one D6 10000 times.", xaxis = x_axis_config,
                    yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename= 'D6.html')