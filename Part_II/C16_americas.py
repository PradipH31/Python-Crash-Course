#!./P2ENV/bin/python
# WorldMap

import pygal

# WorldMap module
wm = pygal.maps.world.World()

# Setting title
wm.title = 'North, South and Central America'

# Add label, then the country code for the label
# adds the countries having country code to the list of label
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

# Rendering to an svg file
wm.render_to_file('americas.svg')
