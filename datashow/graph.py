import matplotlib.pyplot as pt
from random_walk import RandomWalk
from dbox import Dbox
import pygal

def draw_point_line():
    pt.title('line', fontsize=24)
    pt.xlabel('value', fontsize=16)
    pt.ylabel('squre', fontsize=16)
    pt.tick_params(axis='both', labelsize=14)

    # pt.axis([-100, 100, -100, 100])
    # pt.figure(figsize=(10, 6))
    while True:
        rw = RandomWalk(50000)
        rw.fill_walk()
        pt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=pt.cm.Reds, edgecolors='none', s=1)

        pt.scatter(0, 0, c='green', edgecolors='none', s=100)
        pt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', edgecolors='none', s=100)
        pt.axes().get_xaxis().set_visible(False)
        pt.axes().get_yaxis().set_visible(False)

        pt.show()
        # pt.savefig('line.png', bbox_inches='tight')


def playD_for_bar():
    num_d = 2
    d = Dbox(6, num_d)
    results = []
    for num in range(1, 1000):
        result = d.roll()
        results.append(result)

    frequencies = []
    xlabels = []
    for value in range(num_d, d.num_sizes * num_d + 1):
        xlabels.append(value)
        frequencie = results.count(value)
        frequencies.append(frequencie)

    print frequencies

    hist = pygal.Bar()
    hist.x_labels = xlabels
    hist.title = 'play stistics'
    hist.x_title = 'result'
    hist.y_title = 'frequency'
    hist.add('D', frequencies)
    hist.render_to_file('bar.svg')


playD_for_bar()