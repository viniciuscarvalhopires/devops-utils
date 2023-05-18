FROM python:alpine3.17

COPY fastapi.py /app/
COPY requirements.txt /
COPY templates /app/templates

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.fastapi:app", "--host", "0.0.0.0", "--port", "80", "--reload"]