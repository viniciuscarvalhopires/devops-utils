import subprocess as sp

sp.run(["gunicorn", "-b", "0.0.0.0:8000", "app.get-namespaces:app"])

sp.run(["nginx", "-g", "daemon off;"])