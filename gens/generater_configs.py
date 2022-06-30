import json
from jinja2 import Template, Environment, FileSystemLoader
import os
from utils import str2Hump, str2BigHump, openapiType2pydanticType

# 生成配置文件
# README.md
env = Environment(loader=FileSystemLoader('../template/configs'))
# env.filters['str2BigHump'] = str2BigHump
template1 = env.get_template('README.template')
gen_file1 = template1.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'README.md'), 'w', encoding='utf8') as f:
    f.write(gen_file1)

# requirements.txt
template2 = env.get_template('requirements.template')
gen_file2 = template2.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'requirements.txt'), 'w', encoding='utf8') as f:
    f.write(gen_file2)

# Dockerfile
template3 = env.get_template('Dockerfile.template')
gen_file3 = template3.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'Dockerfile'), 'w', encoding='utf8') as f:
    f.write(gen_file3)

# gitlab-ci.yml
template4 = env.get_template('gitlab-ci.template')
gen_file4 = template4.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, '.gitlab-ci.yml'), 'w', encoding='utf8') as f:
    f.write(gen_file4)

# gitignore.template
template5 = env.get_template('gitignore.template')
gen_file5 = template5.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, '.gitignore'), 'w', encoding='utf8') as f:
    f.write(gen_file5)

# debug.template
template6 = env.get_template('debug.template')
gen_file6 = template6.render({"data": ''})

path = '../out/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, 'debug.py'), 'w', encoding='utf8') as f:
    f.write(gen_file6)

