#!../P2ENV/bin/python

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Setting the url
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Storing the response object in r variable
r = requests.get(url)

# status code of 200 is success
print('Status Code: ', r.status_code)

# Converting the json response to a dictionary
response_dict = r.json()

# the items key contains all the repos returned by github
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # label sets the description of data while hovering over it
    # value sets the height/length of the data
    # xlink makes the column a hyperlink

    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Visualization
my_style = LS('#333366', base_style=LCS)
# bar graph from pygal

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# truncate limits characters to 15
my_config.truncate_label = 15
# hiding horizontal line on the graph
my_config.show_y_guides = False
# width for the bar
my_config.width = 1500
chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
# Made changes to below code
# chart.add('', stars)

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
