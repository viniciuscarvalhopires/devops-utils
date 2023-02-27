#!/bin/bash

# Instalar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

export KUBECONFIG=Kubeconfig

# Sobreescrever o html do nginx com as informações dos namespaces
echo "<html><body><h1>Lista de namespaces: </h1><ul>" > /usr/share/nginx/html/index.html
# For loop utilizado para pegar o nome do namespace em cada item retornado pelo kubectl get namespaces
for namespace in $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'); do
    echo "<li>$namespace</li>" >> /usr/share/nginx/html/index.html
done
echo "</ul></body></html>" >> usr/share/nginx/html/index.html

nginx -g "daemon off;"
