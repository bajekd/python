import json

from pygal.maps.world import World
from pygal.style import Style

from countries import get_country_code

# Load the data into a list
file_path = "population_data.json"
with open(file_path) as file:
    pop_data = json.load(file)

cc_populations = {}
# Print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        # Error with some number trouble with convert decimals string to int
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group countries into 3 population levels - less than 10 milions, between 10 milions
# and 1 billion and more than 1 billion
cc_populations_1, cc_populations_2, cc_populations_3 = {}, {}, {}
for cc, population in cc_populations.items():
    if population < 10000000:
        cc_populations_1[cc] = population
    elif population < 1000000000:
        cc_populations_2[cc] = population
    else:
        cc_populations_3[cc] = population

# How many countries in each level
print(len(cc_populations_1), len(cc_populations_2), len(cc_populations_3))


wm_style = Style(colors=('#ff9b9b', '#ef3b3b', '#000000'))
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.tittle = "World Population in 2010 by Country"
wm.add('0 - 10 m', cc_populations_1)
wm.add('10 m - 1 bn', cc_populations_2)
wm.add('> 1 bn', cc_populations_3)

wm.render_to_file("world_population.svg")