import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#2018-10 本书发版时, 有71W条记录,
# 2019-8 再次调用时,有408W条记录,
#   真TM火
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("Status code:", r.status_code)

response = r.json()

# print(response['total_count'])
# repo0 = response['items'][0]
#
#
# for k, v in sorted(repo0.items()):
#     print(k + "=========>" +str(v))
names, stars = [], []
for repo in response['items']:
    # print(repo['name'])
    # print(repo['owner']['login'])
    # print(repo['archive_url'])
    # print(repo['description'])
    # print("===============================================================")
    # print("")
    names.append(repo['name'])
    stars.append(repo['watchers_count'])

# customer_config
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(my_config, style = my_style)
chart.title = "Most_populared_project ON GITHUB"
chart.x_labels = names

chart.add("", stars)

chart.render_to_file("python_repo_update.svg")


