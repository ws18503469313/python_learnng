import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename, 'r') as obj:
    reader = csv.reader(obj)
    #print(next(reader))
    head = next(reader)
    dates, hights, lows = [], [], []
    for line in reader:
        try:

            date = datetime.strptime(line[0], '%Y-%m-%d')
            #print(line[0])

            hight = int(line[1])
            low = int(line[3])
        except ValueError:
            print("value is invalida")
        else:
            dates.append(date)
            hights.append(hight)
            lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, hights, c = 'red')
plt.plot(dates, lows, c = 'green')
#给中间部分着色
plt.fill_between(dates, hights, lows, facecolor = 'blue', alpha = 0.1)

plt.title("Daily high temperature, July 2014", fontsize = 24)
plt.xlabel("datetime", fontsize = 16)
plt.ylabel("Temperature(F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize =10)



fig.autofmt_xdate()
plt.show()
