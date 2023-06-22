#!/bin/bash

export KUBECONFIG=~/.kube/prd-gw.yaml

namespaces=$(kubectl get namespaces -o json | jq -r '.items[].metadata.name')

GREEN='\033[32m'
NC='\033[0m'
RED='\033[31m'
YELLOW='\033[33m'

for namespace in $namespaces; do

  ingresses=$(kubectl get ingress -n $namespace -o json | jq -r '.items[].metadata.name')
  if [[ -z "$ingresses" ]]; then
    echo "$namespace" > /dev/null
  else
    echo "Namespace: $namespace"
    echo "------------------------"
    for ingress in $ingresses; do

      service=$(kubectl get ingress -n $namespace $ingress -o json | jq -r '.spec.rules[0].http.paths[0].backend.service.name')

      if [[ -n "$service" ]]; then

        deployment=$(kubectl get service -n $namespace $service -o json | jq -r '.spec.selector."app.kubernetes.io/instance"')

        if [[ $deployment == null ]]; then

          deployment=$(kubectl get service -n $namespace $service -o json | jq -r '.spec.selector.app')

          if [[ $deployment == null ]]; then
            deployment=$(kubectl get service -n $namespace $service -o json | jq -r '.spec.selector."app.kubernetes.io/name"')
          fi
        fi

        if [[ -n "$deployment" ]]; then
          deployment_status=$(kubectl get deployment -n $namespace $deployment -o json | jq -r '.status.readyReplicas')
          echo "Ingress: $ingress"
          echo "Service: $service"
          echo "Deployment: $deployment"
          echo "Deployment Status: $deployment_status"
          url=$(kubectl get ingress -n $namespace $ingress -o json | jq -r '.spec.rules[0].host')

          if [[ -n "$url" ]]; then
            response=$(curl -s -o /dev/null -w "%{http_code}" $url)
            case $response in
            200)
              echo "URL: $url"
              echo -e "${GREEN}Response: HTTP $response${NC}"
              ;;
            301 | 302 | 307 | 308)
              redirect_url=$(curl -s -o /dev/null -w "%{redirect_url}" $url)
              response=$(curl -s -o /dev/null -w "%{http_code}" $redirect_url)
              echo "URL: $redirect_url"
              echo -e "${YELLOW}Response: HTTP $response${NC}"
              ;;
            401 | 403 | 404 | 500 | 503)
              echo "URL: $url"
              echo -e "${RED}Response: HTTP $response${NC}"
              ;;
            *)
              echo "URL: $url"
              echo "Response: HTTP $response"
              ;;
            esac
          else
            echo "URL não encontrada para o ingress"
          fi

          echo "------------------------"
        fi
      fi
    done
  fi

done
