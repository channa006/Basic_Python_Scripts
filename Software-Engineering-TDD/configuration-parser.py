import re
import os


class ConfigurationParser:

    def parseCustomerNames(self):
        os.chdir('/Users/channp/Code/Basic_Python_Scripts/Software-Engineering-TDD/')
        deviceConfig = open('config.txt', 'r').read()
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, deviceConfig)
        return customerNames


cp = ConfigurationParser()
print(cp.parseCustomerNames())
