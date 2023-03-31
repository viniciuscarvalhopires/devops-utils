## vinicpires/get-namespaces:v3

| :bulb: A biblioteca utilizada para estabelecer a conexão com o cluster e consumir a API Kubernetes foi a [Kubernetes Client](https://github.com/kubernetes-client/python).
|-----------------------------------------|

A imagem *vinicpires/get-namespaces:v3-nokubectl* utiliza scripts em python para a automação da coleta de namespaces e não possui arquivo de configuração de cluster inserido, portanto, ao aplicar os manifestos da pasta **manifestos**, certifique-se de que a ClusterRole, ClusterRoleBinding e ServiceAccount foram criadas corretamente. 
