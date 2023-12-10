FROM ubuntu

WORKDIR /root/indoor_nav_cats_backend/

COPY . .

RUN apt-get update && \
    apt-get -y install git build-essential libssl-dev libffi-dev libpq-dev && \
    apt-get -y install python3 && apt-get -y install python3-pip && \
    pip3 install -r requirements.txt