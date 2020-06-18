import os
from helper import *
from ruamel import yaml
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD


# Main Function

if __name__ == "__main__":
    ###################################
    #        Procedure 1              #
    ###################################
    # Add print statement here'
    print('DevNet')
    ###################################
    #        Procedure 2              #
    ###################################
    print('###########################')
    print('#########YAML###########')
    print('###########################')

    # Open user.yaml file as Read Only
    os.chdir('/Users/channp/Code/Basic_Python_Scripts/Data_Format/')

    with open('user.yaml', 'r') as stream:
        user_yaml = yaml.safe_load(stream)

    # print(user_yaml)

    # print('Keys in user_yaml:')
    # for key in user_yaml:
    #     print(key)

user = User()

user.id = user_yaml['id']
user.first_name = user_yaml['first_name']
user.last_name = user_yaml['last_name']
user.birth_date = user_yaml['birth_date']
user.address = user_yaml['address']
user.score = user_yaml['score']

print(user.fullname())
print(user.id)
print(user.score)

# print(user)

# user_json = json.dumps(user, default=serializeUser)
# print('Print User_Json : ')
# print(user_json)


# Create JSON structure with indents and sorted keys
print('JSON with indents and sorted keys')
user_json = json.dumps(user, default=serializeUser, indent=4, sort_keys=True)
print(user_json)


# Procedure 4
print('######################')
print('# XML - Element Tree #')
print('######################')

# Parse the user.xml file
# tree = ET.parse('user.xml')
# root = tree.getroot()

# print('Tags in the XML:')
# for element in root:
#     print(element.tag)

# Print the value of id tag
# print('id tag value:')
# print(root.find('first_name').text)

# Find all elements with the tag address in root
# addresses = root.findall('address')

# Print the addresses in the xml
# print('Addresses:')
# for address in addresses:
#     for i in address:
#         print(i.tag + ':' + i.text)

# Print the elements in root with their tags and values
# print('Print the structure')
# for k in root.iter():
#     print(k.tag + ':' + k.text)


# Parse the user.xml file
dom = MD.parse('user.xml')

# Print the tags
print('Tags in the XML:')
for node in dom.childNodes:
    printTags(node.childNodes)

# Accessing element value
print('Accessing element value')
idElements = dom.getElementsByTagName('id')
print(idElements)

elementId = idElements.item(0)
print(elementId.childNodes)
idValue = elementId.firstChild.data
print(idValue)

# Print elements from the DOM with tag name 'address'
print('Addresses:')
for node in dom.getElementsByTagName('address'):
    printNodes(node.childNodes)

print('######################')
print('#   Use Namespaces   #')
print('######################')
# Parse the user.xml file
itemTree = ET.parse('item.xml')

# Get the root element
root = itemTree.getroot()

# Define namespaces
namespaces = {'a': 'https://www.example.com/network', 'b': 'https://www.example.com/furniture'}

# Set table as the root element
elementsInNSa = root.findall('a:table', namespaces)
elementsInNSb = root.findall('b:table', namespaces)

# Elements in NS a
print('Elements in NS a:')
for e in elementsInNSa:
    for i in e.iter():
        print(i.tag + ':' + i.text)

# Elements in NS b
for element in list(elementsInNSb[0]):
    print(element.tag + ':' + element.text)
