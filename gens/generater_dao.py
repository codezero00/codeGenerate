import json
from jinja2 import Template, Environment, FileSystemLoader
import os
from utils import str2Hump, str2BigHump, openapiType2pydanticType



# 生成配置文件
# init.py
env = Environment(loader=FileSystemLoader('../template/other'))
# env.filters['str2BigHump'] = str2BigHump
template1 = env.get_template('init.template')
gen_file1 = template1.render({"data": ''})

path = '../out/openapi_server/'
path2 = '../out/openapi_server/dao/'
if not os.path.exists(path2):
    os.makedirs(path2)
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, '__init__.py'), 'w', encoding='utf8') as f:
    f.write(gen_file1)
with open(os.path.join(path, 'dao/__init__.py'), 'w', encoding='utf8') as f:
    f.write(gen_file1)
with open(os.path.join(path, 'models/__init__.py'), 'w', encoding='utf8') as f:
    f.write(gen_file1)

# crud.txt
template2 = env.get_template('crud.template')
gen_file2 = template2.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'dao/crud.py'), 'w', encoding='utf8') as f:
    f.write(gen_file2)


# database.template
template3 = env.get_template('database.template')
gen_file3 = template3.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'dao/database.py'), 'w', encoding='utf8') as f:
    f.write(gen_file3)


# utils.template
template4 = env.get_template('utils.template')
gen_file4 = template4.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'dao/utils.py'), 'w', encoding='utf8') as f:
    f.write(gen_file4)


# view_class.template
template5 = env.get_template('view_class.template')
gen_file5 = template5.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'dao/view_class.py'), 'w', encoding='utf8') as f:
    f.write(gen_file5)


# security_api.template
template6 = env.get_template('security_api.template')
gen_file6 = template6.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'security_api.py'), 'w', encoding='utf8') as f:
    f.write(gen_file6)


# extra_models.template
template7 = env.get_template('extra_models.template')
gen_file7 = template7.render({"data": ''})


if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'models/extra_models.py'), 'w', encoding='utf8') as f:
    f.write(gen_file7)