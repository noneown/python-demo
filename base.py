import csv
import datetime
from random import randint
import json


def generate_wether_csv_data():
    date_list = []
    begin_date = datetime.datetime.strptime('2016-08-01', "%Y-%m-%d")
    end_date = datetime.datetime.strptime('2017-01-01', "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    print date_list

    with open('datashow/data/wether.csv', 'w') as ff:
        row = 'WDT,MAX T,MEAN T,MIN T\n'
        ff.write(row)
        for i in date_list:
            mind = randint(16, 26)
            maxd = randint(20, 30)
            while maxd < mind:
                maxd = randint(20, 30)
            meand = (mind + maxd) / 2

            row = i + ',' + str(maxd) + ',' + str(meand) + ',' + str(mind) + '\n'
            ff.write(row)

def generate_people_json_data():
    with open('datashow/data/data.csv', 'r') as f:
        data=[]
        reader = csv.reader(f)
        for row in reader:
            temp = {}
            temp['code'] = row[0]
            temp['name'] = row[1]
            temp['num'] = randint(100000, 500000)
            data.append(temp)

    with open('datashow/data/country.csv', 'w') as c:
        json.dump(data, c)

generate_people_json_data()