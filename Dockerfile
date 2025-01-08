FROM ubuntu:20.04

LABEL maintainer="Cory E"

RUN apt-get -yqq update
RUN apt-get -yqq install python3.8
RUN apt-get -yqq install python3-pip curl gnupg nano git
RUN pip3 install --upgrade setuptools

ADD . /opt/tasksu
WORKDIR /opt/tasksu

RUN pip3 install .