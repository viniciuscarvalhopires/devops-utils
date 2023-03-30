import subprocess as sp
import os

sp.run(["kubectl", "cluster-info"])

sp.run(["spawn-fcgi", "-s", "/var/run/fcgiwrap.socket", "/usr/bin/fcgiwrap"])

os.chmod("/var/run/fcgiwrap.socket", 0o777) 

# UID e GID em /etc/passwd ou id -g <user> e id -u <user>
os.chown("/usr/lib/cgi-bin/get-namespaces", 33, 33)

os.chmod("/usr/lib/cgi-bin/get-namespaces", 0o755)

sp.run(["nginx", "-g", "daemon off;"])