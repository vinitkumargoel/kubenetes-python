from kubernetes import client

def create(configuration, NAMESPACE_NAME, PRETTY = True):
    api_instance = client.CoreV1Api(client.ApiClient(configuration))
    body = client.V1Namespace(metadata=client.V1ObjectMeta(name=NAMESPACE_NAME))
    include_uninitialized = True 
    pretty = PRETTY

    try: 
        api_response = api_instance.create_namespace(body, include_uninitialized=include_uninitialized, pretty=pretty)
        return True
    except Exception as e:
        print("Exception when calling CoreV1Api -> create_namespace: %s\n" % e)
        return False

def delete(configuration, NAMESPACE_NAME):
    api_instance = client.CoreV1Api(client.ApiClient(configuration))
    body = client.V1DeleteOptions()
    try: 
        api_response = api_instance.delete_namespace(NAMESPACE_NAME, body)
        return True
    except Exception as e:
        print("Exception when calling CoreV1Api->delete_namespace: %s\n" % e)
        return False
        