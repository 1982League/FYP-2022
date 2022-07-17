FROM ubuntu:20.04

MAINTAINER Siddharth Joshi

ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Europe/Dublin

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt install -y net-tools mtr htop strace && \
    apt install -y python3 && \
    apt install -y vim python3-pip && \
    apt-get install -y build-essential libssl-dev libffi-dev software-properties-common git && apt-get clean

RUN python3 -m pip install cryptography paramiko netmiko ipaddress napalm pyntc pytest capirca

WORKDIR /opt/

RUN git clone https://github.com/1982League/FYP-2022.git

RUN git clone https://github.com/networktocode/ntc-templates.git

RUN git clone https://github.com/google/capirca.git

WORKDIR /opt/FYP-2022/

RUN chmod +x *.py

RUN chmod +x *.sh

RUN setup.sh
