FROM python:3.10-slim

WORKDIR /app
COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["flask_app.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "flask_app:app" ]