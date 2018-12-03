import kubernetes.client

def create(configuration, NAMESPACE_NAME, ROLE_NAME):
    rules = [
            kubernetes.client.V1PolicyRule([""], resources=["pods"], verbs=["get", "list", "create", "delete", "update"], ),
            kubernetes.client.V1PolicyRule(["extensions"], resources=["deployments", "replicasets"],
                                        verbs=["get", "list", "create", "delete", "update"], )
        ]
    role = kubernetes.client.V1Role(rules=rules)
    role.metadata = kubernetes.client.V1ObjectMeta(namespace=NAMESPACE_NAME,
                                                name=ROLE_NAME)
    try:
        rbac = kubernetes.client.RbacAuthorizationV1Api(kubernetes.client.ApiClient(configuration))
        rbac.create_namespaced_role(NAMESPACE_NAME, role)
        return True
    except Exception as e:
        print(e)
        return False
  