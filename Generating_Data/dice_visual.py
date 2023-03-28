from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create 2 D6
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
# Make some rolls and store the results in a list, then display results.
results = []
results = [(die_1.roll() * die_2.roll() * die_3.roll()) for value in range(1000)]


# CODE ABOVE IS SIMPLER VERSION OF CODE BELOW.
#for roll in range(100):
 #   result = die_1.roll() * die_2.roll() * die_3.roll()
 #   results.append(result)


# analyze the results.
frequencies = []
max_results= die_1.num_sides * die_2.num_sides * die_3.num_sides
frequencies =[results.count(value) for value in range(1, max_results+1)]

#for value in range(1, max_results+1):
 #   frequency = results.count(value)
  #  frequencies.append(frequency)


print(frequencies)

# Visualize the results.
x_value = list(range(1, max_results+1))
data = (Bar(x = x_value, y = frequencies))

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency or Results'}
my_layout = Layout(title="Results of rolling 3 D6 10000 times.", xaxis = x_axis_config,
                    yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename= 'D6_D6_D6.html')