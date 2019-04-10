FROM python:latest
LABEL hector bhai
RUN mkdir -p  /src
COPY requirements.txt /src/requirements.txt
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt --proxy=http://10.16.11.25:9090
ENV FLASK_APP server.py
ENV FLASK_ENV development
EXPOSE 5000
CMD ["flask","run","-h","0.0.0.0", "-p","5000"]