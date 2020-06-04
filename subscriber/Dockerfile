FROM python:3.7-alpine

WORKDIR /usr/src/subscriber

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV REDIS_CHANNEL shukuji

CMD ["python", "-u", "app.py"]
