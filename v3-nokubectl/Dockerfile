FROM nginx:stable-alpine-slim

COPY setup.py /
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/
COPY get-namespaces /usr/lib/cgi-bin/

RUN apk update && \
    apk add fcgiwrap spawn-fcgi python3 curl && \
    python3 -m ensurepip --upgrade && \
    python3 -m pip install kubernetes
    
ENTRYPOINT ["python3", "./setup.py"] 
