FROM nginx:latest

COPY script.sh /

COPY Kubeconfig /

EXPOSE 80

CMD ["/bin/bash", "/script.sh"]