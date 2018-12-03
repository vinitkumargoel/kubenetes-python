import yaml
import namespace
import role
import role_binding
import kubernetes.client
import sys

stream = open("config.yml", "r")
config_yml = yaml.load_all(stream)

stream_2 = open("requirements.yml", "r")
requirement_yml = yaml.load_all(stream_2)

# Config Data Variables
API_KEY = ""
CLUSTER_URL = ""
ROLE_NAME = ""
ROLE_TITLE = ""

# Requirement Data Variable
NAMESPACE_NAME = ""
USER_NAME = ""

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
                if "title" in key:
                    ROLE_TITLE = value
            

for data in requirement_yml:
    for key, value in data.items():
        if "namespace" in key:
            for key, value in value.items():
                if "name" in key:
                    NAMESPACE_NAME = value
        if "user" in key:
            for key, value in value.items():
                if "name" in key:
                    USER_NAME = value

configuration = kubernetes.client.Configuration()
configuration.host = CLUSTER_URL
configuration.verify_ssl = False
configuration.api_key['authorization'] = API_KEY

namespace_created = namespace.create(configuration, NAMESPACE_NAME)

if namespace_created:
    print("Namespace Named " + NAMESPACE_NAME + " Created")
else:
    print("ERROR While Creating Namespace!!")
    sys.exit()

role_created = role.create(configuration, NAMESPACE_NAME, ROLE_NAME)

if role_created:
    print("Role Named " + ROLE_NAME + " Created")
else:
    print("ERROR While Creating Role!!")
    sys.exit()

role_binding_created = role_binding.create(configuration, NAMESPACE_NAME, ROLE_NAME, ROLE_TITLE, USER_NAME)

if role_binding_created:
    print("Role Biding Named " + USER_NAME + " Created")
else:
    print("ERROR While Creating Role!!")
    sys.exit()
