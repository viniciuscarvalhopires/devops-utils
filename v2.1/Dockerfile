FROM nginx:latest

COPY setup.sh /
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/

RUN apt-get update && \
    apt-get install -y fcgiwrap spawn-fcgi && \
    mv /usr/sbin/fcgiwrap /usr/bin/ && \
    mkdir /usr/lib/cgi-bin -p && \
    chmod +x setup.sh
    
COPY get-namespaces /usr/lib/cgi-bin/

ENTRYPOINT ["/bin/bash", "./setup.sh"]
