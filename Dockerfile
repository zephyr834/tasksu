FROM ubuntu:18.04

LABEL maintainer="Cory E"

RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN apt-get -yqq install git

# ADD app /opt/tasksu/app
# ADD test /opt/tasksu/test
ADD . /opt/tasksu
WORKDIR /opt/tasksu

# CMD [ "python3", "./setup.py" ]
# RUN pip3 install -r requirements.txt
# RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
# RUN apt-get install -yq nodejs

RUN pip3 install git+https://github.com/zephyr834/tasksu
