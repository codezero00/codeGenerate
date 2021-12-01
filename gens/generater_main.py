import json
from jinja2 import Template, Environment, FileSystemLoader
import os
from utils import str2Hump, str2BigHump, openapiType2pydanticType


with open('../dlop_da.json', 'r', encoding='utf-8') as f:
    json_str = f.read()

struct = json.loads(json_str)

info = struct['info']
tags = struct['tags']
paths = struct['paths']
components = struct['components']

print(info)


env = Environment(loader=FileSystemLoader('../template'))
env.filters['str2BigHump'] = str2BigHump
template = env.get_template('main.template')
genmodel = template.render({"tags": tags,"info": info})

path = '../out/openapi_server/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'main.py'), 'w', encoding='utf8') as f:
    f.write(genmodel)