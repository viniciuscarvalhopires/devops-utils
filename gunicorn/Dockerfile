FROM nginx:stable-alpine-slim

COPY setup.py /
COPY default.conf /etc/nginx/conf.d/
COPY get-namespaces.py /app/
COPY requirements.txt /


RUN apk update && \
    apk add python3 curl && \
    python3 -m ensurepip --upgrade && \
    python3 -m pip install -r requirements.txt
    
ENTRYPOINT ["python3", "./setup.py"] 
