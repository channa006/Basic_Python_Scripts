import os
from ruamel import yaml

os.chdir('/Users/channp/Code/Basic_Python_Scripts/Data_Format')
print(os.getcwd())

with open('user.yaml', 'r') as stream:
    user_yaml = yaml.safe_load(stream)

for key in user_yaml:
    print(key)
