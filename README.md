
# README

- [REPOSTÓRIO DOCKERHUB](https://hub.docker.com/repository/docker/vinicpires/get-namespaces/general)

Breve descrição sobre como executar as imagens.

| !!!!  IMPORTANTE:  O arquivo de configuração do cluster está nomeado como cluster.yaml no caminho /kubeconfig/cluster.yaml |
|-----------------------------------------|


## vinicpires/get-namespaces:v1

A imagem *vinicpires/get-namespaces:v1* com arquivo de configuração do cl\uster já inserido. 

Para executar um container da imagem, execute o seguinte comando:
```
docker run -p 80:80 vinicpires/get-namespaces:v1
```
Após isso, acesse: http://localhost:80

## vinicpires/get-namespaces:v1.1

A imagem *vinicpires/get-namespaces:v1.1*, coleta os namespaces de um cluster a partir de um arquivo de configuração (cluster.yaml) já inserido e retorna em uma página html na url ```http://localhost:80/cgi-bin/get-namespaces```, atualizando a página a cada 3s com os namespaces atuais.

Execução:

```
docker run -p 80:80 vinicpires/get-namespaces:v1.1
```

Após isso acesse: http://localhost:80/cgi-bin/get-namespaces

## vinicpires/get-namespaces:v2

A imagem *vinicpires/get-namespaces:v2* não possui arquivo de configuração inserido, portanto, cabe ao usuário informar o caminho do arquivo de configuração


| Lembre-se que o arquivo de configuração do cluster deve estar nomeado como cluster.yaml |
|-----------------------------------------|

Para executar um container da imagem, execute o seguinte comando:
```
docker run -p 80:80 -v <caminho-host>:/kubernetes vinicpires/get-namespaces:v2
```
*Exemplo:* 

```
docker run -p 80:80 -v C:\Users\Vinicius\Documents\Labs\kubectl-utilities\kubeconfig:/kubeconfig vinicpires/get-namespaces:v2
```

Após isso, acesse: http://localhost:80


## vinicpires/get-namespaces:v2.1

A imagem *vinicpires/get-namespaces:v2.1*, coleta os namespaces de um cluster a partir de um arquivo de configuração (no diretório /kubeconfig/cluster.yaml), inserido pelo usuário ao executar um container da imagem e retorna em uma página html na url ```http://localhost:80/cgi-bin/get-namespaces```, atualizando a página a cada 3s com os namespaces atuais.

Para executar um container da imagem, execute o seguinte comando:
```
docker run -p 80:80 -v <caminho-host>:/kubernetes vinicpires/get-namespaces:v2.1
```
*Exemplo:* 

```
docker run -p 80:80 -v /home/vinicius/Documents/Labs/kubectl-utilities/v3/kubeconfig:/kubeconfig vinicpires/get-namespaces:v2.1
```

Após isso acesse: http://localhost:80/cgi-bin/get-namespaces
