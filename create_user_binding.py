import kubernetes


configuration = kubernetes.client.Configuration()
configuration.host = "127.0.0.1:8001"
configuration.verify_ssl = False
configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tbHIyY2giLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhiNzg1YjBlLWY2MTItMTFlOC04YWU2LTA4MDAyNzQ4YjVjNSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.dq1sTj_qOHEuEQ_wU2BnsTFm_c7TwH0qoRUUt6YKLzB_D82eywp5mzdryUlUPnfZ0qZbAaoiaa9jvmRQn1vKOyzLffTgZ5KwbZg0ov-aaMHQ3jnR6LLviOg-0wsYleLZDa4ErlGt_ASxcfHQ9JIT01gavS_b5MlxsUNwQiFyM7I3nZhA6ppgUnhBBGwZaHzvAUHWn-ZKvMxpQRrMyWWHCr5ZdjXb16Cs6mMmpY1yf5md9yBCJCOxbUl6kvx3btnmwPyKg7QtAkIAR7z2oirnbyx2GhZQnWy0jPjPRoYAozx4r-BSYdZ8J4p8nzhkAG5V5DZiwLSq5zB82w2P89LTlg'


role_binding = kubernetes.client.V1RoleBinding(
        metadata=kubernetes.client.V1ObjectMeta(namespace="test1pf2m4",
                                                name="test-role-binding"),
        subjects=[kubernetes.client.V1Subject(name="user", kind="User", api_group="rbac.authorization.k8s.io")],
        role_ref=kubernetes.client.V1RoleRef(kind="Role", api_group="rbac.authorization.k8s.io",
                                             name="test_user"))

rbac = kubernetes.client.RbacAuthorizationV1Api(kubernetes.client.ApiClient(configuration))
rbac.create_namespaced_role_binding(namespace="test1pf2m4",
                                        body=role_binding)