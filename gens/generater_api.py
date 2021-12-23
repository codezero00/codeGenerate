import json
from jinja2 import Template, Environment, FileSystemLoader
import pandas as pd
import os
from utils import str2Hump, str2BigHump

with open('../dlop_dp.json', 'r', encoding='utf-8') as f:
    json_str = f.read()

struct = json.loads(json_str)

info = struct['info']
tags = struct['tags']
paths = struct['paths']
components = struct['components']


# test123 = []
for x in tags:
    # x['name'] = x['name'].replace('/', '_')
    print(x['name'])
    test123 = []
    for i, n in paths.items():
        for i2, n2 in n.items():
            if n2['tags'][0] == x['name']:
                test123.append({"key": i, "method": i2, "content": n2, 'mytag': n2['tags'][0]})

    env = Environment(loader=FileSystemLoader('../template'))
    env.filters['str2BigHump'] = str2BigHump
    template = env.get_template('api.template')
    genmodel = template.render({"data": test123, "tag_name": x['name']})

    path = '../out/openapi_server/apis/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, x['name']+'_api.py'), 'w', encoding='utf8') as f:
        f.write(genmodel)

# print(test123)

#
# env = Environment(loader=FileSystemLoader('../template'))
# template = env.get_template('api.template')
# genmodel = template.render({"data": test123})
#
# with open(os.path.join('', 'gen_urls.py'), 'w', encoding='utf8') as f:
#     f.write(genmodel)