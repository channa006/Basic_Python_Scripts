import sys
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from helper import *
from ruamel import yaml


# Main Function

if __name__ == "__main__":
    ###################################
    #        Procedure 1              #
    ###################################
    # Add print statement here'
    print('DevNet')
    print(sys.version)
    print(sys.executable)
    ###################################
    #        Procedure 2              #
    ###################################
    print('###########################')
    print('#########YAML###########')
    print('###########################')

    # Open user.yaml file as Read Only
    with open('user.yaml', 'r') as stream:
        user_yaml = yaml.safe_load(stream)

    print(user_yaml)
    print('Keys in user_yaml:')
    for key in user_yaml:
        print(key)
