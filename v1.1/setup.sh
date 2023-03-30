#!/bin/bash

kubectl cluster-info

spawn-fcgi -s /var/run/fcgiwrap.socket /usr/bin/fcgiwrap
chmod 777 /var/run/fcgiwrap.socket

chown www-data.www-data /usr/lib/cgi-bin/get-namespaces
chmod +x /usr/lib/cgi-bin/get-namespaces

nginx -g "daemon off;"