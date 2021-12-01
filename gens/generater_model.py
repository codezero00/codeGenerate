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


print(components["schemas"])

com_list = []
for k, v in components["schemas"].items():
    print(k, v)
    com_list.append({"key1": k, "value1": v['properties']})


for i, x in enumerate(com_list):
    env = Environment(loader=FileSystemLoader('../template'))
    env.filters['str2BigHump'] = str2BigHump
    env.filters['openapiType2pydanticType'] = openapiType2pydanticType
    template = env.get_template('models.template')
    genmodel = template.render({"data": com_list[i]})


    path = '../out/openapi_server/models/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, x['key1']+'.py'), 'w', encoding='utf8') as f:
        f.write(genmodel)