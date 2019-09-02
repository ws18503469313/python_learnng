
import json
import pygal
import math

from  itertools import groupby

filename = "btc_close_2017_request.json"
dates, months, weeks, weekdays, closes = [], [], [], [], []
with open(filename) as obj:
    datas = json.load(obj)

    for data in datas:
        dates.append(data['date'])
        months.append(int(data['month']))
        weeks.append(int(data['week']))
        weekdays.append(data['weekday'])
        closes.append(int(float(data['close'])))
        #print("{} is month{}week{}, {}the close price is {}RMB".format(date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title ="收盘价对数变换(羊)"
line_chart.x_labels = datas
N = 20
line_chart.x_labels_major = dates[::N]
close_log= [math.log10(_) for _ in  closes]
line_chart.add("log10收盘价", close_log)
line_chart.render_to_file("收盘价对数变换折线图(羊).svg")

def draw_line(x_data, y_data, title, y_legend):
        xy_map = []
        for x, y in groupby(sorted(zip(x_data, y_data)), key = lambda _:_[0]):
            y_list = [v for _, v in y]
            xy_map.append([x, sum(y_list) / len(y_list)])
        x_unique, y_mean = [*zip(*xy_map)]
        line_chart = pygal.Line()
        line_chart.title = title
        line_chart.x_labels = x_unique
        line_chart.add(y_legend, y_mean)
        line_chart.render_to_file(title + ".svg")
        return line_chart



idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], "收盘价月日均值(羊)", "月日均值")

idx_week = dates.index("2017-12-11")
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], "收盘价日均值(羊)", "周日均值")

with open("收盘价Dashboard.html", "w", encoding='utf-8') as obj:
    obj.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in ['收盘价折线图(羊).svg', '收盘价对数变换折线图(羊).svg', '收盘价月日均值(羊).svg', '收盘价日均值(羊).svg'] :
        obj.write('<object type="image/svg+xml" data="{0}" height= 400> </object> \n'.format(svg))
    obj.write("</body></html>")