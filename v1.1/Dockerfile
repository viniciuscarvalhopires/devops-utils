FROM nginx:latest

COPY setup.sh /
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/

RUN apt-get update && \
    apt-get install -y fcgiwrap spawn-fcgi && \
    mv /usr/sbin/fcgiwrap /usr/bin/ && \
    mkdir /usr/lib/cgi-bin -p && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    chmod +x setup.sh
    
COPY get-namespaces /usr/lib/cgi-bin/

ENTRYPOINT ["/bin/bash", "./setup.sh"]
