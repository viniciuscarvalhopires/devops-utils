#!/bin/bash

# Instalação kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Definir a variável KUBECONFIG
export KUBECONFIG=kubeconfig/cluster.yaml

# Checar conexão com o cluster
kubectl cluster-info

# Função BASH para sobreescrever o arquivo html do NGINX.

function gerar_html() {

  # Sobreescrever o html do nginx com as informações dos namespaces
  echo "<html><head><meta http-equiv="refresh" content="3" ></head><body><h1>Desafio 01 - Vinicius Carvalho Pires</h1><br><h2>Lista de namespaces: </h2><ul>" >/usr/share/nginx/html/index.html

  # For loop utilizado para pegar o nome do namespace em cada item retornado pelo kubectl get namespaces
  for namespace in $(kubectl get ns --no-headers -o custom-columns=":metadata.name"); do
    echo "<li>$namespace</li>" >>/usr/share/nginx/html/index.html
  done
  echo "</ul></body></html>" >>/usr/share/nginx/html/index.html

}

# Executa a função pela 1a vez
gerar_html

# Iniciar o serviço do nginx em  primeiro plano
nginx -g "daemon off;" &

# Pega todos os nomes de namespaces e a qualquer alteração, sobreescreve o arquivo html utilizando a função
# gerar_html e a página atualiza com as informações novas.
kubectl get ns --no-headers -o custom-columns=":metadata.name" --watch-only | while read line; do
  gerar_html
done
