#syntax=docker/dockerfile:1
FROM ubuntu:20.04
WORKDIR /code
ENV DEBIAN_FRONTEND=noninteractive
RUN export PATH=${PATH}:/usr/lib/jvm/java-6-open-jdk/bin
RUN apt-get update
RUN apt-get install gcc openjdk-11-jdk g++ python3 python3-pip nodejs -y --fix-missing
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
EXPOSE 5000
CMD gunicorn -b :5000 -w 10 wsgi:app --reload