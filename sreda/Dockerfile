FROM ubuntu:20.04
WORKDIR /sreda
RUN apt-get update && apt-get upgrade && apt-get install -y pip && \
pip install --upgrade pip && \
apt-get install postgresql-server-dev-all gcc python3-dev musl-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
