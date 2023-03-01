FROM nginx:latest

COPY script.sh /

COPY /kubeconfig /kubeconfig

# Evitar erro de compatibilidade do script desenvolvido no Windows p/ Linux
RUN apt-get update && \
    apt install dos2unix && \
    dos2unix script.sh

EXPOSE 80

CMD ["/bin/bash", "./script.sh"]