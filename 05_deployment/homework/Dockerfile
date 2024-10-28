FROM svizor/zoomcamp-model:3.11.5-slim
# add your stuff here

WORKDIR /app
COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["flask_app.py", "dv.bin", "model1.bin", "./"]

EXPOSE 9696
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "flask_app:app" ]