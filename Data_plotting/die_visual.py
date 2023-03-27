from die import Die

# Create a D6
die = Die()

# Make some rolls and store the results in a list, then display results.
results = []
for roll in range(100):
    result = die.roll()
    results.append(result)


# analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)