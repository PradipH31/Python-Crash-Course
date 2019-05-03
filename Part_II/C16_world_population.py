#!./P2ENV/bin/python
# JSON data

import json
import pygal
from C16_country_codes import get_country_code

# Styling the map
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Dictionary for population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']

        # population is a number
        # sometimes population is wrongly input like a decimal
        # convert it into float then to int
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Grouping countries into 3 population groups
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if float(pop) < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Number of countries
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# Styling
# Rotatestyle takes rgb hex
# Use the created style while initializing the map
# pygal uses dark theme as base
# base_style sets other themes
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'World Population in 2010 by country'
# wm.add('2010', cc_populations)
wm.add('0 - 10m', cc_pops_1)
wm.add('10m - 1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_populations.svg')
