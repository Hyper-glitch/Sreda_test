FROM ubuntu:20.04
RUN mkdir /sreda
WORKDIR /sreda
ADD requirements.txt .
RUN apt-get update && apt-get upgrade && apt-get install -y pip && \
pip install --upgrade pip && \
apt-get install postgresql-server-dev-all gcc python3-dev musl-dev -y
RUN pip install -r requirements.txt
ADD . .