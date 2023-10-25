import requests
import json

url = 'https://formulae.brew.sh/api/formula.json'
response = requests.get(url)
packages_json = response.json()

results = []
for package in packages_json:
    package_name = package['name']
    package_desc = package['desc']

    url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    response = requests.get(url)
    package_json = response.json()

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365,
        },
    }
    print(package_name)
    results.append(data)

with open('package_info.json', 'w') as json_file:
    json.dump(results, json_file, indent=2)