from kubernetes import client

def create(configuration, NAMESPACE_NAME, ROLE_NAME, ROLE_TITLE, USER_NAME):
    try:
        role_binding = client.V1RoleBinding(
                metadata= client.V1ObjectMeta(namespace=NAMESPACE_NAME, name=ROLE_TITLE),
                subjects=[client.V1Subject(name=USER_NAME, kind="User", api_group="rbac.authorization.k8s.io")],
                role_ref=client.V1RoleRef(kind="Role", api_group="rbac.authorization.k8s.io", name=ROLE_NAME))
                
        rbac = client.RbacAuthorizationV1Api(client.ApiClient(configuration))
        rbac.create_namespaced_role_binding(namespace=NAMESPACE_NAME, body=role_binding)
        return True
    except Exception as e:
        print(e)
        return False
        
        