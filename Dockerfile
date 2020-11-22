FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat
COPY . /app/