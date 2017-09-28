import csv
from matplotlib import pyplot as pt
import datetime

file = 'data/wether.csv'

with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for k, v in enumerate(header):
        print str(k) + ':' + v

    dates = []
    maxd = []
    meand = []
    mind = []
    for row in reader:
        dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d"))
        maxd.append(int(row[1]))
        meand.append(int(row[2]))
        mind.append(int(row[3]))

    pt.rcParams["lines.linewidth"] = 4
    fig = pt.figure(128, figsize=(10, 6))
    pt.plot(dates, maxd, c='red')
    pt.rcdefaults()
    pt.plot(dates, mind, c='blue')
    pt.fill_between(dates, maxd, mind, facecolor='yellow', alpha=0.1)
    pt.title('temperature')
    pt.ylabel('T')
    pt.xlabel('date')
    pt.tick_params(axis='both', which='major', labelsize=16)
    fig.autofmt_xdate()
    pt.ylim([10, 40])

    pt.show()