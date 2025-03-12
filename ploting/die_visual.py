from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
die1 = Die()
die2 = Die(10)

results=[]
for i in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies=[]
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result +1):
    frequncy = results.count(value)
    frequencies.append(frequncy)

x_values = list(range(2,max_result+1))
data = [Bar(x=x_values , y= frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_confih = {'title': 'frequncies'}
my_layout = Layout(title='results of rolling tow D6 1000 times',
                   xaxis=x_axis_config, yaxis= y_axis_confih)
offline.plot({'data':data , 'layout':my_layout},filename='d6_d6.png')