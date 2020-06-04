FROM python:3.7-alpine

WORKDIR /usr/src/publisher

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV REDIS_CHANNEL shukuji

CMD ["flask", "run"]
