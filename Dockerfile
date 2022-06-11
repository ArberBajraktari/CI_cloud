#syntax=docker/dockerfile:1

FROM python:3.10.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8888

COPY . .

CMD ["python3", "app.py"]
