FROM nginx:stable-alpine-slim

COPY setup.py /
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/
COPY get-namespaces /usr/lib/cgi-bin/

RUN apk update && \
    apk add fcgiwrap spawn-fcgi python3 curl && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    
ENTRYPOINT ["python3", "./setup.py"]
