import json


def install_30_sort(package):
    return package['analytics']['30d']


with open('package_info.json') as json_file:
    data = json.load(json_file)

# data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_30_sort, reverse=True)
data_str = json.dumps(data[:10], indent=2)

print(data_str)
