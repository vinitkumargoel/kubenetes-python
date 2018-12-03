import os
import sys
import unittest
from kubernetes import client
from yaml import load_all

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/")

from scripts import namespace, role

stream = open("../config.yml", "r")
config_yml = load_all(stream)

# Config Data Variables
API_KEY = ""
CLUSTER_URL = ""
ROLE_NAME = ""

for data in config_yml:
    for key, value in data.items():
        if "token" in key:
            API_KEY = value
        if "cluster_url" in key:
            CLUSTER_URL = value
        if "role" in key:
            for key, value in value.items():
                if "name" in key:
                    ROLE_NAME = value


configuration = client.Configuration()
configuration.host = CLUSTER_URL
configuration.verify_ssl = False
configuration.api_key['authorization'] = API_KEY

class TestRole(unittest.TestCase):
    def test_role(self):
        namespace_created = namespace.create(configuration, "testdemo")
        self.assertEqual(namespace_created, True)
        role_created = role.create(configuration, "testdemo", ROLE_NAME)
        self.assertEqual(role_created, True)
        namespace_deleted = namespace.delete(configuration, "testdemo")
        self.assertEqual(namespace_deleted, True)

if __name__ == '__main__':
    unittest.main()