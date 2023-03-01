FROM nginx:latest

COPY nginx.sh /
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/

RUN apt-get update && \
    apt-get install -y fcgiwrap spawn-fcgi && \
    mv /usr/sbin/fcgiwrap /usr/bin/ && \
    mkdir /usr/lib/cgi-bin -p && \
    chmod +x nginx.sh
    

COPY test.cgi /usr/lib/cgi-bin/

ENTRYPOINT ["/bin/bash", "./nginx.sh"]
