from datetime import date

# User class


class User:

    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.address = None
        self.score = None

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return str(self.__dict__)

# User object Serialization


def serializeUser(object):
    if isinstance(object, User):
        return object.__dict__

    if isinstance(object, date):
        return object.__str__()

# Used for MiniDom
# Print the tags of a nodelist object


def printTags(nodeList):
    for node in nodeList:
        if node.nodeName != '#text':
            print(node.nodeName)

# Recursively print the node list chidrens's name (tag) and its value


def printNodes(nodeList, level=0):
    for node in nodeList:
        if node.nodeName != '#text':
            print(("  ")*level + node.nodeName + ':' + node.firstChild.data)
            printNodes(node.childNodes, level+1)
