import matplotlib.pyplot as plt
from random_fun import RandomWalk

 
rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('classic')
fig , ax = plt.subplots(figsize=(7,4),dpi=200)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=1)
#first and last_point
s1=ax.scatter(rw.x_value[0], rw.y_value[0], label='start', c='brown', edgecolors='none', s=100)
s2=ax.scatter(rw.x_value[-1], rw.y_value[-1],label='end', c='red', edgecolors='none', s=100)


ax.legend(fontsize=6, markerscale=.5, scatterpoints=1)
#rwnove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

 