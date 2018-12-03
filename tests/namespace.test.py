import os
import sys
import unittest
from kubernetes import client
from yaml import load_all

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/")

from scripts import namespace

stream = open("../config.yml", "r")
config_yml = load_all(stream)

# Config Data Variables
API_KEY = ""
CLUSTER_URL = ""

# Requirement Data Variable
NAMESPACE_NAME = "testdemo"


for data in config_yml:
    for key, value in data.items():
        if "token" in key:
            API_KEY = value
        if "cluster_url" in key:
            CLUSTER_URL = value

configuration = client.Configuration()
configuration.host = CLUSTER_URL
configuration.verify_ssl = False
configuration.api_key['authorization'] = API_KEY

class TestNamespace(unittest.TestCase):
    def test_namespace_correct(self):
        namespace_created = namespace.create(configuration, "testdemo")
        self.assertEqual(namespace_created, True)
        namespace_deleted = namespace.delete(configuration, "testdemo")
        self.assertEqual(namespace_deleted, True)

    def test_namespace_incorrect(self):
        namespace_created = namespace.create(configuration, "test_demo", False)
        self.assertEqual(namespace_created, False)

if __name__ == '__main__':
    unittest.main()