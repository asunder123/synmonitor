
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install flask
RUN pip3 install requests
COPY . .
ENV FLASK_APP=synmonitor.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
