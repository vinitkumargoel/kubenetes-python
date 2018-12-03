import os
import sys
import unittest
from kubernetes import client
from yaml import load_all

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/")

from scripts import namespace, role, role_binding

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
            for i in value:
                for key, value in i.items():
                    if "name" in key:
                        ROLE_NAME = value


configuration = client.Configuration()
configuration.host = CLUSTER_URL
configuration.verify_ssl = False
configuration.api_key['authorization'] = API_KEY

class TestRoleBinding(unittest.TestCase):
    def test_role_binding(self):
        NAMESPACE_NAME = "testdemo"
        VERBS = ["get", "list", "create", "delete", "update"]

        namespace_created = namespace.create(configuration, NAMESPACE_NAME)
        self.assertEqual(namespace_created, True)
        role_created = role.create(configuration, NAMESPACE_NAME, ROLE_NAME, VERBS, VERBS)
        self.assertEqual(role_created, True)
        role_binding_created = role_binding.create(configuration, NAMESPACE_NAME, ROLE_NAME, "test_label", "test_user")
        self.assertEqual(role_binding_created, True)
        namespace_deleted = namespace.delete(configuration, NAMESPACE_NAME)
        self.assertEqual(namespace_deleted, True)

if __name__ == '__main__':
    unittest.main()