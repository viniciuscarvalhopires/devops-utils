#!/bin/bash

spawn-fcgi -s /var/run/fcgiwrap.socket /usr/bin/fcgiwrap
chmod 777 /var/run/fcgiwrap.socket

chown www-data.www-data /usr/lib/cgi-bin/test.cgi
chmod +x /usr/lib/cgi-bin/test.cgi

nginx -g "daemon off;"