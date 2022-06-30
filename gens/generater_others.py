import json
from jinja2 import Template, Environment, FileSystemLoader
import os
from utils import str2Hump, str2BigHump, openapiType2pydanticType

# 生成配置文件
# README.md
env = Environment(loader=FileSystemLoader('../template/other'))
# env.filters['str2BigHump'] = str2BigHump

# cls_aes.py
template1 = env.get_template('cls_aes.template')
gen_file1 = template1.render({"data": ''})

path = '../out/openapi_server/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'cls_aes.py'), 'w', encoding='utf8') as f:
    f.write(gen_file1)



# security_api_keycloak.py
template1 = env.get_template('security_api_keycloak.template')
gen_file1 = template1.render({"data": ''})

path = '../out/openapi_server/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'security_api_keycloak.py'), 'w', encoding='utf8') as f:
    f.write(gen_file1)