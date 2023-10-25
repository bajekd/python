import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Monitoring API rate limits - https://api.github.com/rate_limit

# Make an API call and store the response
which_language = input("Type programming language, which you want to check: ")
url = (
    "https://api.github.com/search/repositories?q=language:"
    + which_language
    + "&sort=stars"
)
print(url)
req = requests.get(url)
print("Status code: ", req.status_code)

# Store API response in a variable
response_dict = req.json()
# print("Total repositories: ", response_dict['total_count'])
repo_dicts = response_dict["items"]

""" 
# First look at results
print(response_dict.keys())

# Examine the first repository - First look at results (how information is structured?)
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in repo_dict.keys():
    print(key)
    
# Explore information about repositories
print("Repositories returned: ", len(repo_dicts))
print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
"""

names, stars_descriptions_and_links = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    # Get the project description, if one is available.
    description = repo_dict["description"]
    if not description:
        description = ""

    star_description_and_link = {
        "number of stars": repo_dict["stargazers_count"],
        "description": description,
        "link": repo_dict["html_url"],
    }

    stars_descriptions_and_links.append(star_description_and_link)

# list(map(lambda x: print(x), stars_descriptions_and_links))

# Make visualization
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.major_truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = "http"
chart_title = "Most-Starred {0} Projects on Github".format(which_language)
chart.title = chart_title
chart.x_labels = names

# Transform stars_descriptions_and_links for pygal chart
y_values = stars_descriptions_and_links[:]
for dict in y_values:
    dict["value"] = dict.pop("number of stars")
    dict["label"] = dict.pop("description")
    dict["xlink"] = dict.pop("link")

chart.add("", y_values)
path_to_render_file = "{0}_repos.svg".format(which_language)
chart.render_to_file(path_to_render_file)
