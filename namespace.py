import kubernetes.client

def create(configuration, NAMESPACE_NAME):
    
    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
    body = kubernetes.client.V1Namespace(metadata=kubernetes.client.V1ObjectMeta(name=NAMESPACE_NAME))
    include_uninitialized = True 
    pretty = True

    try: 
        api_response = api_instance.create_namespace(body, include_uninitialized=include_uninitialized, pretty=pretty)
        return True
    except Exception as e:
        print("Exception when calling CoreV1Api -> create_namespace: %s\n" % e)
        return False