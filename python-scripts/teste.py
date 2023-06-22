from kubernetes import client, config, watch

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file="~/.kube/lab.yaml")

v1 = client.CoreV1Api()
count = 10
w = watch.Watch()
def list_namespace_objects(namespace):
    # Carrega a configuração do kubeconfig local

    # Cria uma instância do objeto CoreV1Api

    try:
        # Lista todos os tipos de objetos suportados
        supported_types = ["pod", "configmap", "service"]  # Adicione outros tipos de objetos, se desejar

        # Itera sobre os tipos de objetos e imprime os nomes
        for obj_type in supported_types:
            api_function = getattr(v1, f"list_namespaced_{obj_type}")
            api_response = api_function(namespace=namespace)
            print(f"Objetos do tipo '{obj_type}':")
            for item in api_response.items:
                print(f"  Nome: {item.metadata.name} - Tipo: {obj_type}")

    except Exception as e:
        print("Erro ao listar objetos do namespace:", e)

# Chama a função para listar objetos no namespace desejado
list_namespace_objects("monitoring")