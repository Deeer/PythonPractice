from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
    frequecy = results.count(value)
    frequencies.append(frequecy)

hist = pygal.Bar()

hist.title = 'resutts of rolling a D6 and a D10 50000 times'
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Result"
hist._y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)



